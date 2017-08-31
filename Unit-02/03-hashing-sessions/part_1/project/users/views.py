from flask import redirect, render_template, request, url_for, Blueprint, session, flash, g
from project.users.forms import UserForm
from project.users.models import User
from project import db,bcrypt

from sqlalchemy.exc import IntegrityError

from functools import wraps

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

@users_blueprint.before_request
def current_user():
    if session.get('user_id'):
        g.current_user = User.query.get(session['user_id'])
    else:
        g.current_user = None

@users_blueprint.route('/signup', methods =["GET", "POST"])
def signup():
    form = UserForm(request.form)
    if request.method == 'POST':
        if form.validate():
            try:
                new_user = User(form.data['username'], form.data['password'])
                db.session.add(new_user)
                db.session.commit()
            except IntegrityError as e:
                flash('Username is already taken.')
                return render_template('signup.html', form=form)
            return redirect(url_for('users.login'))
        if form.is_submitted():
            flash("Invalid submission. Please try again.")
    return render_template('signup.html', form=form)


@users_blueprint.route('/login', methods = ["GET", "POST"])
def login():
    form = UserForm(request.form)
    if request.method == 'POST':
        if form.validate():
            found_user = User.query.filter_by(username = form.data['username']).first()
            if found_user:
                authenticated_user = bcrypt.check_password_hash(found_user.password, form.data['password'])
                if authenticated_user:
                    session["user_id"] = found_user.id
                    return redirect(url_for('users.welcome'))
    return render_template('login.html', form=form)

@users_blueprint.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been signed out.')
    return redirect(url_for('users.login'))

@users_blueprint.route('/welcome')
@ensure_logged_in
def welcome():
    return render_template('welcome.html')

@users_blueprint.route('/<int:id>')
@ensure_logged_in
def show(id):
    user = User.query.get(id)
    return render_template('/show.html', user=user)

@users_blueprint.route('/<int:id>/edit')
@ensure_logged_in
def edit(id):
    user = User.query.get(id)
    if session['user_id'] == id:
        return render_template('/edit.html', user=user)
    return redirect(url_for('users.welcome'))
