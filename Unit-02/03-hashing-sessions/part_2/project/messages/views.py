from flask import Blueprint, render_template, request, redirect, url_for, abort
from project.messages.models import Message
from project.users.models import User
from project.messages.forms import CreateForm, EditForm
from project import db
from flask_wtf.csrf import validate_csrf

messages_blueprint = Blueprint('messages', __name__, template_folder='templates')

@messages_blueprint.route('/', methods = ['GET','POST'])
def index(user_id):
    user = User.query.get(user_id)
    if request.method == 'POST':
        form = CreateForm(request.form)
        if form.validate():
            new_message = Message(request.form['text'], user.id)
            db.session.add(new_message)
            db.session.commit()
            return redirect(url_for('messages.index', user_id=user.id))
        return render_template('messages/new.html', user=user, form=form)
    return render_template('messages/index.html', user=user)

@messages_blueprint.route('/new')
def new(user_id):
    user = User.query.get(user_id)
    form = CreateForm()
    return render_template('messages/new.html', user=user, form=form)

@messages_blueprint.route('/<int:id>', methods = ['GET','PATCH','DELETE'])
def show(user_id, id):
    message = Message.query.get(id)
    user = User.query.get(user_id)
    if message == None:
        abort(404)
        
    if request.method == b'PATCH':
        edit_form = EditForm(request.form)
        if edit_form.validate():
            message.text = request.form.get('text')
            db.session.add(message)
            db.session.commit()
            return redirect(url_for('messages.index', user_id = user_id))
        return render_template('messages/edit.html', message = message, edit_form = edit_form)

    if request.method == b'DELETE':
        if validate_csrf(request.form.get('csrf_token')) is None:
            db.session.delete(message)
            db.session.commit()
            return redirect(url_for('messages.index', user_id = user.id))
    return render_template('messages/show.html', user_id=user.id, message=message)

@messages_blueprint.route('/<int:id>/edit')
def edit(user_id, id):
    message = Message.query.get(id)
    form = EditForm(obj=message)
    return render_template('messages/edit.html', message=message, form=form)
