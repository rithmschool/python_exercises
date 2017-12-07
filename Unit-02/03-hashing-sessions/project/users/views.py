from flask import redirect, render_template, request, url_for, Blueprint, session, flash, g
from project.users.forms import UserForm, LoginForm, DeleteForm
from project.models import User, Message
from project import db, bcrypt
from functools import wraps

from sqlalchemy.exc import IntegrityError


users_blueprint = Blueprint(
	'users',
	__name__,
	template_folder='templates'
	)

def ensure_logged_in(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not session.get('user_id'):
            flash("Please log in first")
            return redirect(url_for('users.login'))
        return fn(*args, **kwargs)
    return wrapper

def ensure_correct_user(fn):
    # make sure we preserve the corrent __name__, and __doc__ values for our decorator
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # in the params we have something called id, is it the same as the user logged in?
        if kwargs.get('id') != session.get('user_id'):
            # if not, redirect them back home
            flash("Not Authorized")
            return redirect(url_for('users.welcome'))
        # otherwise, move on with all the arguments passed in!
        return fn(*args, **kwargs)
    return wrapper

@users_blueprint.route('/messages')
def messages():
    messages = Message.query.all()
    return render_template('users/messages.html', messages=messages)

@users_blueprint.route('/welcome')
@ensure_logged_in
def welcome():
    return render_template('users/welcome.html', users=User.query.all())


@users_blueprint.route('/signup', methods =["GET", "POST"])
def signup():
    form = UserForm(request.form)
    if request.method == "POST" and form.validate():
        try:
            new_user = User(form.data['first_name'], form.data['last_name'], form.data['username'], form.data['password'])
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
    return render_template('users/login.html', form=form)

@users_blueprint.before_request
def current_user():
    if session.get('user_id'):
        g.current_user = User.query.get(session['user_id'])
    else:
        g.current_user = None

@users_blueprint.route('/<int:id>', methods=['GET','PATCH', 'DELETE'])
@ensure_logged_in
@ensure_correct_user
def show(id):
    delete_form = DeleteForm()
    found_user = User.query.get(id)
    if request.method == b'PATCH':
        form = UserForm(request.form)
        if form.validate():
            found_user.first_name = form.first_name.data
            found_user.last_name = form.last_name.data
            found_user.username = form.username.data
            found_user.password = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
            db.session.add(found_user)
            db.session.commit()
            flash('User Updated!')
            return redirect(url_for('users.welcome'))
        return render_template('users/edit.html', user=found_user, form=form, delete_form=delete_form)
    if request.method == b'DELETE':
        delete_form = DeleteForm(request.form)
        if delete_form.validate():
            db.session.delete(found_user)
            db.session.commit()
            session.pop('user_id', None)
            flash('User Deleted!')
            return redirect(url_for('users.welcome'))
    return render_template('users/show.html', user=found_user, delete_form=delete_form)

@users_blueprint.route('/<int:id>/edit')
@ensure_logged_in
@ensure_correct_user
def edit(id):
    delete_form = DeleteForm()
    found_user = User.query.get(id)
    user_form = UserForm(obj=found_user)
    return render_template('users/edit.html', user=found_user, form=user_form, delete_form=delete_form)

@users_blueprint.route('/logout')
def logout():
  session.pop('user_id', None)
  flash('You have been signed out.')
  return redirect(url_for('users.login'))
