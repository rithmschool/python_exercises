from flask import Flask, redirect, render_template, url_for, flash, request, Blueprint
from project.users.forms import UserForm, DeleteForm
from project.users.models import User
from project import db

users_blueprint = Blueprint('users', __name__, template_folder='templates')

@users_blueprint.route('/', methods=["GET", "POST"])
def index():
	if request.method == "POST":
		form = UserForm(request.form)
		if form.validate():
			created_user = User(form.username.data, form.email.data, form.first_name.data, form.last_name.data)
			db.session.add(created_user)
			db.session.commit()
			flash("You have successfully created a new user!")
			return redirect(url_for('users.index'))
		return render_template('users/new.html', form=form)
	return render_template('users/index.html', users=User.query.all())

@users_blueprint.route('/new')
def new():
	form = UserForm()
	return render_template('users/new.html', form=form)

@users_blueprint.route('/<int:user_id>', methods=['GET', 'PATCH', 'DELETE'])
def show(user_id):
	user = User.query.get(user_id)
	if request.method == b"PATCH":
		form = UserForm(request.form)
		if form.validate():
			user.username = form.username.data
			user.email = form.email.data
			user.first_name = form.first_name.data
			user.last_name = form.last_name.data
			db.session.add(user)
			db.session.commit()
			flash("You have successfully edited this user.")
			return redirect(url_for('users.index'))
		flash("Please enter proper values for each field.")
		return redirect(url_for('users.edit', user_id=user_id, form=form))
	if request.method == b"DELETE":
		delete_form = DeleteForm(request.form)
		if delete_form.validate():
			db.session.delete(user)
			db.session.commit()
			flash("You've successfully deleted {}".format(user.username))
			return redirect(url_for('users.index'))
		return render_template('users/show.html', delete_form=delete_form, user=user)
	return render_template('users/show.html', user=user)

@users_blueprint.route('/<int:user_id>/edit')
def edit(user_id):
	user = User.query.get(user_id)
	form = UserForm(obj=user)
	delete_form = DeleteForm(obj=user)
	return render_template('users/edit.html', user=user, form=form, delete_form=delete_form)