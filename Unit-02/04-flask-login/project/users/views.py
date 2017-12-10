from flask import Blueprint, render_template, request, redirect, url_for, flash
from project.users.forms import UserForm, LoginForm, DeleteForm
from project import db, bcrypt
from project.models import User
from sqlalchemy.exc import IntegrityError
from project.decorators import prevent_login_signup, ensure_correct_user
from flask_login import login_user, logout_user, login_required


users_blueprint = Blueprint(
	'users',
	__name__,
	template_folder = 'templates'
)

@login_required
@users_blueprint.route('/')
def index():
	return render_template('users/index.html', users=User.query.all())


@users_blueprint.route('/signup', methods=["GET","POST"])
@prevent_login_signup
def signup():
	form = UserForm(request.form)
	if form.validate():
		try:
			new_user = User(
				form.first_name.data, 
				form.last_name.data,
				form.username.data,
				form.password.data)
			db.session.add(new_user)
			db.session.commit()
			login_user(new_user)
			flash('User Created!')
			return redirect(url_for('users.index'))
		except IntegrityError as e:
			flash('Username already taken')
			return render_template('users/signup.html', form=form)
	return render_template('users/signup.html', form=form)
	

@users_blueprint.route('/login', methods=["GET", "POST"])
@prevent_login_signup
def login():
	form = LoginForm(request.form)
	if request.method == "POST":
		if form.validate():
			authenticated_user = User.authenticate(form.username.data, form.password.data)
			if authenticated_user:
				login_user(authenticated_user)
				flash("You are now logged in!")
				return redirect(url_for('users.index'))
			else:
				flash('Invalid Credentials')
				return redirect(url_for('users.login'))	
	return render_template('users/login.html', form=form)

# @users_blueprint.route('/signup')
# @prevent_login_signup
# def new():
# 	user_form = UserForm()
# 	return render_template('users/signup.html', form=user_form)

@users_blueprint.route('/<int:id>/edit')
@login_required
@ensure_correct_user
def edit(id):
	found_user = User.query.get(id)
	user_form = UserForm(obj=found_user)
	delete_form = DeleteForm()
	return render_template('users/edit.html', user=found_user, form=user_form, delete_form=delete_form)

@users_blueprint.route('/<int:id>', methods=["GET", "PATCH", "DELETE"])
@login_required
@ensure_correct_user
def show(id):
	found_user = User.query.get(id)
	delete_form = DeleteForm()
	if request.method == b"PATCH":
		form = UserForm(request.form)
		if form.validate():
			found_user.first_name = form.first_name.data
			found_user.last_name = form.last_name.data
			found_user.username = form.username.data
			found_user.password = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
			time = db.func.now()
			found_user.updated_on = time
			db.session.add(found_user)
			db.session.commit()
			flash('User Updated!')
			return redirect(url_for('users.index')) 
		return render_template('users/edit.html', user=found_user, form=form, delete_form=delete_form)
	if request.method ==b"DELETE":
		delete_form = DeleteForm(request.form)
		if delete_form.validate():
			db.session.delete(found_user)
			db.session.commit()
			logout_user()
			flash('User Deleted!')
			return redirect(url_for('users.login'))
	return render_template('users/show.html', user=found_user)

@users_blueprint.route('/logout')
@login_required
def logout():
	logout_user()
	flash('Logged Out!')
	return redirect(url_for('users.login'))