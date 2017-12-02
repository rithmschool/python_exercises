from flask import Blueprint, url_for, redirect, render_template, request
from project.models import User
from project.forms import UserForm, DeleteForm
from project import db

users_blueprint = Blueprint(
	'users',
	__name__,
	template_folder='templates/users'
)

@users_blueprint.route("/", methods = ["GET", "POST"])
def index():
	if request.method == "POST":
		form = UserForm(request.form)
		if form.validate():
			user = User(form.first_name.data, form.last_name.data)
			db.session.add(user)
			db.session.commit()
			return redirect(url_for('users.index'))
		return render_template('new.html', form=form)	
	users = User.query.all() 
	return render_template('index.html', users=users)

@users_blueprint.route("/new")
def new():
	form = UserForm()
	return render_template('new.html', form=form)

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
			return redirect(url_for('users.index'))
		return render_template('edit.html', user=user, form=form)
	if request.method == b"DELETE":
		delete_form = DeleteForm(request.form)
		if delete_form.validate():
			db.session.delete(user)
			db.session.commit()
		return redirect(url_for('users.index'))
	delete_form = DeleteForm()
	return render_template('show.html', user=user, delete_form=delete_form)

@users_blueprint.route("/<int:id>/edit")
def edit(id):
	user = User.query.get(id)
	form = UserForm(obj=user)
	return render_template('edit.html', user=user, form=form)