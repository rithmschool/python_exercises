# we will import much more later
from flask import Blueprint, render_template, url_for, redirect, flash, request, session
from project.users.forms import UserForm, DeleteForm, LoginForm
from project.models import User
from project import db, bcrypt
from functools import wraps

from sqlalchemy.exc import IntegrityError

# let's create the owners_blueprint to register in our __init__.py
users_blueprint = Blueprint(
    'users',
    __name__,
    template_folder='templates/users'
)


def ensure_logged_in(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not session.get('user_id'):
            flash("Please log in first")
            return redirect(url_for('users.login'))
        return fn(*args, **kwargs)
    return wrapper


@users_blueprint.route("/", methods=["GET", "POST"])
def index():
    form = UserForm(request.form)
    if request.method == "POST" and form.validate():
      try:
        found_user = User.query.filter_by(username=form.username.data).first()
        if found_user:
          flash("Invalid Credentials")
        new_user = User(form.data['first_name'], form.data['last_name'], form.data['username'], form.data['password'])
        db.session.add(new_user)
        db.session.commit()
        return render_template("welcome.html")
      except IntegrityError as e:
        return render_template("new.html", form=form)
    return render_template("index.html", users=User.query.all())

  # form = UserForm(request.form)
  #   if request.method == "POST" and form.validate():
  #       try:
  #           new_user = User(form.data['username'], form.data['password'])
  #           db.session.add(new_user)
  #           db.session.commit()
  #       except IntegrityError as e:
  #           return render_template('signup.html', form=form)
  #       return redirect(url_for('users.login'))
  #   return render_template('signup.html', form=form)


@users_blueprint.route("/new")
def new():
    user_form = UserForm()
    return render_template('new.html', form=user_form)


@users_blueprint.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm(request.form)
    if request.method == "POST" and login_form.validate():
        found_user = User.query.filter_by(
            username=login_form.username.data).first()
        if found_user:
            authenticated_user = bcrypt.check_password_hash(
                found_user.password, login_form.password.data)
            if authenticated_user:
                session['user_id'] = found_user.id
                return redirect(url_for('users.welcome'))
        else:
          flash('Invalid Credentials')
    return render_template('login.html', form=login_form)


@users_blueprint.route("/welcome")
@ensure_logged_in
def welcome():
    return render_template('welcome.html')

@users_blueprint.route('/logout')
def logout():
  session.pop('user_id', None)
  flash('You have been signed out.')
  return redirect(url_for('users.login'))

@users_blueprint.route("/<int:id>", methods=["GET", "PATCH", "DELETE"])
def show(id):
    delete_form = DeleteForm(request.form)
    found_user = User.query.get(id)
    if request.method == b"PATCH":
        form = UserForm(request.form)
        if form.validate():
            found_user.first_name = request.form.get('first_name')
            found_user.last_name = request.form.get('last_name')
            db.session.add(found_user)
            db.session.commit()
            flash("User Updated!!!")
            return redirect(url_for('users.index'))
        return render_template("edit.html", user=found_user, form=user_form)
    if request.method == b"DELETE":
      if delete_form.validate():
        db.session.delete(found_user)
        db.session.commit()
        flash("User Deleted!!!")
      return redirect(url_for('users.index'))
    return render_template("show.html", user=found_user, delete_form=delete_form)


@users_blueprint.route("/<int:id>/edit")
def edit(id):
    found_user = User.query.get(id)
    user_form = UserForm(obj=found_user)
    return render_template("edit.html", user=found_user, form=user_form)
