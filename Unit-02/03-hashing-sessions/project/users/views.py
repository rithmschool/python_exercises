from flask import Blueprint, redirect, render_template, url_for, request, flash, g, session 
from project.users.models import User
from project.messages.models import Message
from project.users.forms import UserForm, DeleteForm, LoginForm
from project.decorators import ensure_correct_user, ensure_logged_in
from project import db, bcrypt

from sqlalchemy.exc import IntegrityError
users_blueprint = Blueprint('users', __name__, template_folder='templates')


@users_blueprint.route('/signup', methods =["GET", "POST"])
def signup():
    form = UserForm(request.form)
    if request.method == "POST" and form.validate():
        try:
            new_user = User(form.data['username'],
            				form.data['password'],
            				form.data['first_name'],
            				form.data['last_name'])
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError as e:
            flash("Invalid submission. Please try again.")
            return render_template('users/signup.html', form=form)
        return redirect(url_for('users.login'))
    return render_template('users/signup.html', form=form)

@users_blueprint.route('/login', methods = ["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.authenticate(form.data['username'], form.data['password'])
        if user:
            session['user_id'] = user.id
            flash("You've successfully logged in!")
            return redirect(url_for('users.welcome'))
        flash("Invalid credentials. Please try again.")
    return render_template('users/login.html', form=form)

@users_blueprint.before_request
def current_user():
    if session.get('user_id'):
        g.current_user= User.query.get(session['user_id'])
    else:
        g.current_user = None    

@users_blueprint.route('/welcome')
@ensure_logged_in
def welcome():
    return render_template('users/welcome.html', users=User.query.all())    

@users_blueprint.route('/logout')    
def logout():
    session.pop('user_id', None)
    flash('You have been logged out, fren.')
    return redirect(url_for('users.login'))

@users_blueprint.route('/<int:id>', methods=['GET','PATCH','DELETE'])
def show(id):
    found_user = User.query.get(id)
    delete_form = DeleteForm()
    if request.method == b'PATCH':
        form = UserForm(request.form)
        if form.validate():
            found_user.username = form.username.data
            found_user.password = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
            found_user.first_name = form.first_name.data
            found_user.last_name = form.last_name.data
            db.session.add(found_user)
            db.session.commit()
            flash('User updated!')
            return redirect(url_for('users.welcome'))
        return render_template('users/edit.html', user=found_user, form=form)	
    if request.method ==b'DELETE':
        delete_form = DeleteForm(request.form) 
        if delete_form.validate():
            db.session.delete(found_user)
            db.session.commit()
            session.pop('user_id', None)
            flash('User deleted!')
            return redirect(url_for('users.welcome')) 
    return render_template('users/show.html', user=found_user, delete_form=delete_form)

@users_blueprint.route('/<int:id>/edit')
@ensure_logged_in
@ensure_correct_user
def edit(id):
    user = User.query.get(id)
    delete_form = DeleteForm()
    user_form = UserForm(obj=user) #use obj to prepopulate forms
    return render_template('users/edit.html', user=user, form=user_form, delete_form=delete_form)	

@users_blueprint.route('/messages')
def messages():
    messages = Message.query.all()
    return render_template('users/messages.html', messages = messages)
