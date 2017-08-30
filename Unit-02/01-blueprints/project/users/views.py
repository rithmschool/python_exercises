from flask import Blueprint, Flask, render_template, request, redirect, flash, url_for, abort
from project.users.models import User
from project.users.forms import CreateForm, EditForm
from project import db
from flask_wtf.csrf import validate_csrf

users_blueprint = Blueprint('users', __name__, template_folder='templates')

@users_blueprint.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        form = CreateForm(request.form)
        if form.validate():
            new_user = User(request.form['username'], 
                            request.form['first_name'],
                            request.form['last_name'],
                            request.form['email'])
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('users.index'))
        return render_template('users/new.html', form = form)
    return render_template('users/index.html', users = User.query.all())

@users_blueprint.route('/new')
def new():
    return render_template('users/new.html', form = CreateForm())

@users_blueprint.route('/<int:id>', methods = ['GET','PATCH','DELETE'])
def show(id):
    user = User.query.get(id)
    if request.method == b'PATCH':
        form = EditForm(request.form)
        if form.validate():
            user.username = request.form.get('username')
            user.first_name = request.form.get('first_name')
            user.last_name = request.form.get('last_name')
            user.email = request.form.get('email')
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('users.index'))
        render_template('users/edit.html', user=user, form=form)

    if request.method == b'DELETE':
        if validate_csrf(request.form.get('csrf_token')) is None:
            db.session.delete(user)
            db.session.commit()
            return redirect(url_for('users.index'))    
    return render_template('users/show.html', user=user)

@users_blueprint.route('/<int:id>/edit')
def edit(id):
    user = User.query.get(id)
    form = EditForm(obj=user)
    return render_template('users/edit.html', user=user, form=form)
