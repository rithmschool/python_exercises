from flask import redirect, render_template, request, url_for, Blueprint, abort, flash
from project.users.models import User
from project.users.forms import UserLoginForm, UserForm, EditUserForm, DeleteUserForm
from project import db
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, logout_user, login_required, current_user
from project.decorators import ensure_correct_user

users_blueprint = Blueprint(
	'users',
	__name__,
	template_folder='templates'
)

@users_blueprint.route('/signup', methods =["GET", "POST"])
def signup():
  form = UserForm(request.form)
  if request.method == "POST" and form.validate():
    try:
    	new_user = User(request.form.get('username'), request.form.get('password'), 
    		request.form.get('first_name'), request.form.get('last_name'),
    		 request.form.get('email'))
    	db.session.add(new_user)
    	db.session.commit()
    	flash("You have successfully signed up!")
    except IntegrityError as e:
      flash("Invalid submission. Please try again.")
      return render_template('users/signup.html', form=form)
    return redirect(url_for('users.login'))
  return render_template('users/signup.html', form=form)

@users_blueprint.route('/', methods=['GET'])
@login_required
def index():
	if(current_user.is_admin):
		return render_template('users/index.html', users=User.query.order_by(User.username).all())
	
	flash("Not Authorized")
	return render_template('users/not_auth.html')

@users_blueprint.route('/login', methods = ["GET", "POST"])
def login():
  form = UserLoginForm(request.form)
  if request.method == "POST":
  	if form.validate():
  		user = User.authenticate(form.data['username'], form.data['password'])
  		if user:
  			login_user(user)
  			flash("You've successfully logged in!")
  			return redirect(url_for('users.show', id=user.id))
  	flash("Invalid credentials. Please try again.")
  return render_template('users/login.html', form=form)

@users_blueprint.route('/new')
def new():
	form = UserForm(request.form)
	return render_template('users/new.html', form=form)

@users_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
@ensure_correct_user
def show(id):
	found_user = User.query.filter_by(id=id).first()

	if found_user is None:
		abort(404)

	if request.method == b"DELETE":
		d_form = DeleteUserForm(request.form)
		if d_form.validate():			
			db.session.delete(found_user)
			db.session.commit()
			flash("You have successfully deleted User {}".format(found_user.username))
			return redirect(url_for('users.index'))
		else:
			# e_form = EditUserForm(obj=found_user)
			# return render_template('users/edit.html', user=found_user, d_form=d_form, e_form=e_form)
			return redirect(url_for('users.show', id=found_user.id))

	if request.method == b"PATCH":
		e_form = EditUserForm(request.form)
		if e_form.validate():
			found_user.username = request.form.get('username')
			found_user.first_name = request.form.get('first_name')
			found_user.last_name = request.form.get('last_name')
			found_user.email = request.form.get('email')
			db.session.add(found_user)
			db.session.commit()
			flash("You have successfully updated a User!")
			return redirect(url_for('users.show', id=found_user.id))
			# return redirect(url_for('users.index'))
		else:
			d_form = DeleteUserForm()
			return render_template('users/edit.html', user=found_user, d_form=d_form, e_form=e_form)

	return render_template('users/show.html', user=found_user)

@users_blueprint.route('/<int:id>/edit', methods=['GET'])
@ensure_correct_user
def edit(id):
	found_user = User.query.filter_by(id=id).first()
	e_form = EditUserForm(obj=found_user)
	d_form = DeleteUserForm()

	if found_user is None:
		abort(404)

	return render_template('users/edit.html', user=found_user, e_form=e_form, d_form=d_form)

@users_blueprint.route('/logout')
def logout():
	logout_user()
	flash('You have been signed out.')
	return redirect(url_for('users.login'))