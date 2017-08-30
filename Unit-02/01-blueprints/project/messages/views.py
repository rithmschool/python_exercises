from flask import redirect, render_template, request, url_for, flash, Blueprint
from project.messages.models import Message
from project.users.models import User
from project.messages.forms import MessageForm
from flask_wtf.csrf import validate_csrf, ValidationError
from project import db

messages_blueprint = Blueprint(
    'messages',
    __name__,
    template_folder='templates'
)

@messages_blueprint.route('/', methods=['GET', 'POST'])
def index(user_id):
    form = MessageForm(request.form)
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        if form.validate():
            message = Message(request.form['content'], user.id)
            db.session.add(message)
            db.session.commit()
            flash("Success")
            return redirect(url_for('messages.index', user_id=user.id))
        else:
            error = "errors need a fixing"
            return render_template('messages/new.html', user=user, form=form, error=error)
    return render_template('messages/index.html', user=user, form=form)

@messages_blueprint.route('/new')
def new(user_id):
    form = MessageForm(request.form)
    user = User.query.get_or_404(user_id)
    return render_template('messages/new.html', user=user, form=form)

@messages_blueprint.route('/<int:message_id>', methods=['GET','PATCH','DELETE'])
def show(user_id, message_id):
    user = User.query.get_or_404(user_id)
    message = Message.query.get_or_404(message_id)
    form = MessageForm(request.form, obj=message)
    if request.method == b'PATCH':
        if form.validate():
            form.populate_obj(message)
            db.session.add(message)
            db.session.commit()
            flash("Message Updated")
            return redirect(url_for('messages.show', user_id=user.id, message_id=message.id))
        else:
            error = "Err, attention required"
            return render_template('messages/edit.html', user=user, message=message, form=form, error=error)
    if request.method == b'DELETE':
        try:
            validate_csrf(request.form.get('csrf_token'))
        except ValidationError:
            delete_e = "Message couldn't be deleted"
            return render_template('messages/show.html', user=user, message=message, delete_e=delete_e)
        db.session.delete(message)
        db.session.commit()
        flash("Message deleted")
        return redirect(url_for('messages.index', user_id=user.id))
    return render_template('messages/show.html', user=user, message=message)

@messages_blueprint.route('/<int:message_id>/edit')
def edit(user_id, message_id):
    user = User.query.get_or_404(user_id)
    message = Message.query.get_or_404(message_id)
    form = MessageForm(request.form, obj=message)
    return render_template('messages/edit.html', user=user, message=message, form=form)
