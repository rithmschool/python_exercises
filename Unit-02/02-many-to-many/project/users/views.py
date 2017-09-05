from flask import redirect, render_template, request, url_for,Blueprint, flash
from project.models import User, Message
from project.users.forms import UserForm
from project import db

users_blueprint = Blueprint(
    'users',
    __name__,
    template_folder='templates'
)

@users_blueprint.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    form = UserForm(request.form)
    if form.validate_on_submit():
      flash("You have succesfully signed up!")
      db.session.add(User( \
          request.form.get('username'),\
          request.form.get('email'), \
          request.form.get('firstname'),\
          request.form.get('lastname'), \
          request.form.get('img_url')))
      db.session.commit()
      return redirect(url_for('users.index'))
    return render_template('users/new.html', form=form)
  return render_template('users/index.html', users=User.query.all(), messages=Message.query.all())

@users_blueprint.route('/new')
def new():
    form = UserForm()
    return render_template('users/new.html', form=form)

@users_blueprint.route('/<int:id>/edit')
def edit(id):
  found_user = User.query.get_or_404(id)
  form = UserForm(obj=found_user)
  return render_template('users/edit.html', users=found_user, form=form)

@users_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):
  found_user = User.query.get_or_404(id)
  if request.method == b"PATCH":
    form = UserForm(request.form)
    if form.validate():
      flash("Update Successful")
      found_user.username = request.form.get('username')
      found_user.email = request.form.get('email')
      found_user.firstname = request.form.get('firstname')
      found_user.lastname = request.form.get('lastname')
      found_user.img_url = request.form.get('img_url')
      db.session.add(found_user)
      db.session.commit()
      return redirect(url_for('users.index'))
    return render_template('users/edit.html', users=found_user, form=form)
  if request.method == b"DELETE":
    flash("User Deleted")
    db.session.delete(found_user)
    db.session.commit()
    return redirect(url_for('users.index'))
  return render_template('users/show.html', users=found_user)
