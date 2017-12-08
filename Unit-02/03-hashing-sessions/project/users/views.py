from flask import Blueprint, url_for, redirect, render_template, request, flash
from project.models import User
from project import db
from project.forms import UserForm, DeleteForm, LoginForm
from sqlalchemy.exc import IntegrityError
from project.decorators import ensure_authenticated, ensure_correct_user, prevent_loginsignup
from flask_login import login_user, logout_user, login_required

users_blueprint = Blueprint(
	'users',
	__name__,
	template_folder='templates'
)

@users_blueprint.route('/')
@login_required
def index():
	delete_form = DeleteForm()
	return render_template('users/index.html', users=User.query.all(), delete_form=delete_form)

@users_blueprint.route("/", methods = ["POST"])
def signup():
	form = UserForm(request.form)
	if request.method == "POST" and form.validate():
		try:
			new_user = User(form.first_name.data, form.last_name.data, form.username.data, form.password.data)
			db.session.add(new_user)
			db.session.commit()
			login_user(new_user)
			flash('User Created')
			return redirect(url_for('users.index'))
		except IntegrityError as e:
			return render_template('users/new.html', form=form)	
	return render_template('users/new.html', form=form)	
	

@users_blueprint.route("/new")
@prevent_loginsignup
def new():
	form = UserForm(request.form)
	return render_template('users/new.html', form=form)

@users_blueprint.route('/login', methods = ["GET", "POST"])
@prevent_loginsignup
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        authenticated_user = User.authenticate(form.username.data, form.password.data)
        if authenticated_user:
        	login_user(authenticated_user)
        	flash('You are logged in!')
        	return redirect(url_for('users.index'))
        else: 
            flash("invalid credentials")
            return redirect(url_for('users.login'))
    return render_template('users/login.html', form=form)

@users_blueprint.route('/welcome')
def welcome():
    return "Welcome"

@users_blueprint.route("/<int:id>", methods = ["GET", "PATCH", "DELETE"])
@ensure_authenticated
@ensure_correct_user
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
@ensure_authenticated
@ensure_correct_user
def edit(id):
	user = User.query.get(id)
	form = UserForm(obj=user)
	return render_template('users/edit.html', user=user, form=form)


@users_blueprint.route('/logout')
@ensure_authenticated
def logout():
	login_user()
	flash('Logged out!')
	return redirect('users.login')
