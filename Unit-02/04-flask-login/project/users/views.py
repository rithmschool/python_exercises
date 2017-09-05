from flask import redirect, render_template, request, url_for,Blueprint, flash
from project.models import User
from project.users.forms import UserForm, UserLogin
from functools import wraps
from flask_login import login_user, logout_user, current_user, login_required
from project import db, bcrypt

from sqlalchemy.exc import IntegrityError

users_blueprint = Blueprint(
    'users',
    __name__,
    template_folder='templates'
)

def ensure_correct_user(fn):
  @wraps(fn)
  def wrapper(*args, **kwargs):
    if kwargs.get('id') != current_user.id:
      flash('Not Authorized')
      return redirect(url_for('users.index'))
    return fn(*args, **kwargs)
  return wrapper


@users_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
  form = UserForm(request.form)
  if request.method == 'POST' and form.validate_on_submit():
      flash("You have succesfully signed up!")
      try:
        new_user = User(
          form.data['username'],\
          form.data['password'],\
          form.data['email'], \
          form.data['firstname'],\
          form.data['lastname'],\
          form.data['img_url']
          )
        db.session.add(new_user)
        db.session.commit()
      except IntegrityError as e:
        flash("Username already taken")
        return render_template('signup.html', form=form)
      return redirect(url_for('users.index'))
  return render_template('users/signup.html', form=form)

@users_blueprint.route('/login', methods = ['GET', 'POST'])
def login():
  form = UserLogin(request.form)
  if request.method == 'POST' and form.validate():
    user = User.authenticate(form.data['username'], form.data['password'])
    if user:
      login_user(user)
      flash("Welcome!")
      return redirect(url_for('users.show', id=user.id))
    else:
      flash("Invalid Credentials")
  return render_template('users/login.html', form=form)

@users_blueprint.route('/logout')
@login_required
def logout():
  flash('You have been signed out.')
  logout_user()
  return redirect(url_for('users.index'))


@users_blueprint.route('/')
def index():
  return render_template('users/index.html', users=User.query.all())

@users_blueprint.route('/<int:id>/edit')
@login_required
@ensure_correct_user
def edit(id):
  # https://github.com/rithmschool/python_curriculum/blob/master/Unit-02/examples/flask_login/project/users/views.py
  found_user = User.query.get_or_404(id)
  form = UserForm(obj=found_user)
  return render_template('users/edit.html', user=found_user, form=form)

@users_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
@login_required
@ensure_correct_user
def show(id):
  found_user = User.query.get_or_404(id)
  if request.method == b"PATCH":
    form = UserForm(request.form)
    if form.validate():
      flash("Update Successful")
      found_user.username = form.data['username']
      found_user.password = bcrypt.generate_password_hash(form.data['password']).decode('UTF-8')
      found_user.email = form.data['email']
      found_user.firstname = form.data['firstname']
      found_user.lastname = form.data['lastname']
      found_user.img_url = form.data['img_url']
      db.session.add(found_user)
      db.session.commit()
      return redirect(url_for('users.index'))
    return render_template('users/edit.html', users=found_user, form=form)
  if request.method == b"DELETE":
    flash("User Deleted")
    db.session.delete(found_user)
    db.session.commit()
    logout_user()
    return redirect(url_for('users.index'))
  return render_template('users/show.html', users=found_user)
