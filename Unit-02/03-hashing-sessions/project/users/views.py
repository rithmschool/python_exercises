from flask import Blueprint, url_for, redirect, render_template, request, flash
from project.models import User
from project.forms import UserForm, DeleteForm, LoginForm
from project import db, bcrypt
from sqlalchemy.exc import IntegrityError

users_blueprint = Blueprint(
	'users',
	__name__,
	template_folder='templates/users'
)

@users_blueprint.route("/", methods = ["GET", "POST"])
def index():
	form = UserForm(request.form)
	if request.method == "POST" and form.validate():
		try:
			user = User(form.first_name.data, form.last_name.data, form.username.data, form.password.data)
			db.session.add(user)
			db.session.commit()
			flash('User Created')
			return redirect(url_for('users.index'))
		except IntegrityError as e:
			return render_template('new.html', form=form)	
	return render_template('index.html', users=User.query.all())

@users_blueprint.route("/new")
def new():
	form = UserForm(request.form)
	return render_template('new.html', form=form)

@users_blueprint.route('/login', methods = ["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        found_user = User.query.filter_by(username=form.data['username']).first()
        if found_user:
            authenticated_user = bcrypt.check_password_hash(found_user.password, form.data['password'])
            if authenticated_user:
                return redirect(url_for('users.welcome'))
    return render_template('login.html', form=form)

@users_blueprint.route('/welcome')
def welcome():
    return "Welcome"

@users_blueprint.route("/<int:id>", methods = ["GET", "PATCH", "DELETE"])
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
		return render_template('edit.html', user=user, form=form)
	if request.method == b"DELETE":
		delete_form = DeleteForm(request.form)
		if delete_form.validate():
			db.session.delete(user)
			db.session.commit()
			flash('User Deleted')
		return redirect(url_for('users.index'))
	delete_form = DeleteForm()
	return render_template('show.html', user=user, delete_form=delete_form)

@users_blueprint.route("/<int:id>/edit")
def edit(id):
	user = User.query.get(id)
	form = UserForm(obj=user)
	return render_template('edit.html', user=user, form=form)