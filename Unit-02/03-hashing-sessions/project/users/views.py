from flask import redirect, render_template, request, url_for, Blueprint, flash, session
from project.users.forms import UserForm
from project.users.models import User
from project import db, bcrypt
from functools import wraps
from flask_wtf.csrf import validate_csrf, ValidationError
from sqlalchemy.exc import IntegrityError

users_blueprint = Blueprint(
    'users',
    __name__,
    template_folder='templates'
);

def ensure_logged_in(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not session.get('user_id'):
            flash("Please Log In")
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

def function_name(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get('id') != session.get('user_id'):
            flash("Not Authorized")
            return redirect(url_for('users.welcome'))
        return fn(*args, **kwargs)
    return wrapper

@users_blueprint.route('/signup', methods=["GET", "POST"])
def signup():
    form = UserForm(request.form)
    if form.validate():
        try:
            new_user = User(form.data['username'], form.data['password'])
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError as e:
            return render_template('signup.html', form=form)
        return redirect(url_for('users.login'))
    return render_template('signup.html', form=form)

@users_blueprint.route('/login', methods=["GET", "POST"])
def login():
    form = UserForm(request.form)
    if form.validate():
        found_user = User.authenticate(form.data['username'], form.data['password'])
        if found_user:
            session['user_id'] = found_user.id
            flash("Welcome to the app!")
            return redirect(url_for('users.welcome'))
    if form.is_submitted():
        flash("Invalid credentials. Please try again.")
    return render_template('login.html', form=form)

@users_blueprint.route('/welcome')
@ensure_logged_in
def welcome():
    users = User.query.all()
    return render_template('welcome.html', users=users)

@users_blueprint.route('/logout')
@ensure_logged_in
def logout():
    session.pop('user_id', None)
    flash("You have been signed out")
    return redirect(url_for('user.login'))

@users_blueprint.route('/<int:id>', methods=["GET", "PATCH", "DELETE"])
@ensure_logged_in
def show(id): # delete and patch - Must be sure we're logged in as the correct user
    found_user = User.query.get(id)
    user_is_current_user = (found_user.id == session['user_id'])
    if request.method == b"PATCH": # handle business and move on to index
        if not user_is_current_user: # just in case they got here somehow without using Edit.html
            flash("Not Authorized")
            return redirect(url_for('user.show'), user=found_user)
        form = UserForm(request.form)
        found_user.username = form.username.data
        db.session.add(found_user)
        db.session.commit()
        flash("User Updated!")
        return redirect(url_for('users.welcome'))
    if request.method == b"DELETE": # handle business and move on to index
        if not user_is_current_user: # just in case they got here somehow without using Edit.html
            flash("Not Authorized")
            return redirect(url_for('users.show'), user=found_user)
        try:
            validate_csrf(request.form.get('csrf_token'))
        except ValidationError:
            return redirect(url_for('users.show'))
        db.session.delete(found_user)
        db.session.commit()
        flash("User Deleted!")
        return redirect(url_for('users.signup'))
    return render_template('show.html', user=found_user, authorized=user_is_current_user)

@users_blueprint.route('/<int:id>/edit')
@ensure_correct_user
def edit(id):
    found_user = User.query.get(id)
    form = UserForm(obj=found_user)
    return render_template('edit.html', user=found_user, form=form)



