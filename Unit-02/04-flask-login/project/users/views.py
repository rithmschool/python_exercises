from flask import Blueprint, url_for, redirect, render_template, request, flash, session, g
from project.models import User
from project.forms import UserForm, DeleteForm, LoginForm
from project import db, bcrypt
from sqlalchemy.exc import IntegrityError
from project.decorators import prevent_login_signup, ensure_authorization
from flask_login import login_user, logout_user, login_required #why import from flask as opposed to loginmanager or app

users_blueprint = Blueprint(
	'users',
	__name__,
	template_folder='templates'
)

@users_blueprint.route("/")
def index():
	return render_template('users/index.html', users=User.query.all()) 

@users_blueprint.route("/", methods = ["POST"])
def signup():
	form = UserForm(request.form)
	if request.method == "POST" and form.validate():
		try:
			user = User(form.first_name.data, form.last_name.data, form.username.data, form.password.data)
			db.session.add(user)
			db.session.commit()
			login_user(user)
			flash('User Created')
			return redirect(url_for('users.index'))
		except IntegrityError as e:
			flash('Username Taken')
			return render_template('users/new.html', form=form)		

@users_blueprint.route("/new")
@prevent_login_signup
def new():
	form = UserForm(request.form)
	return render_template('users/new.html', form=form)

@users_blueprint.route('/login', methods = ["GET", "POST"])
@prevent_login_signup
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        authenticated_user = User.authenticate(form.username.data, form.password.data)
        if authenticated_user:
        	login_user(authenticated_user)
        	flash('Logged In!')
        	return redirect(url_for('users.index'))
        flash('Invalid Credentials')
    return render_template('users/login.html', form=form)

@users_blueprint.route("/<int:id>", methods = ["GET", "PATCH", "DELETE"])
@ensure_authorization
def show(id):
	user = User.query.get(id)
	if request.method == b"PATCH":
		form = UserForm(request.form)
		if form.validate():
			user.first_name = form.first_name.data
			user.last_name = form.last_name.data
			db.session.add(user)
			db.session.commit()
			flash('User Updated')
			return redirect(url_for('users.index'))
		return render_template('users/edit.html', user=user, form=form)
	if request.method == b"DELETE":
		delete_form = DeleteForm(request.form)
		if delete_form.validate():
			db.session.delete(user)
			db.session.commit()
			logout_user()
			flash('User Deleted')
		return redirect(url_for('users.index'))
	delete_form = DeleteForm()
	return render_template('users/show.html', user=user, delete_form=delete_form)

@users_blueprint.route("/<int:id>/edit")
@ensure_authorization
def edit(id):
	user = User.query.get(id)
	form = UserForm(obj=user)
	return render_template('users/edit.html', user=user, form=form)

@users_blueprint.route("/logout")
def logout():
	logout_user()
	flash('Logged Out!')
	return redirect(url_for('users.login'))