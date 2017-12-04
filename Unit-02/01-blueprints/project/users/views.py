from flask import render_template, url_for, redirect, request, flash, Blueprint
from project.users.forms import UserForm, DeleteForm
from project.users.models import User
from project import db

users_blueprint= Blueprint(
	'users',
	__name__,
	template_folder = 'templates/users'
	)

@users_blueprint.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		user_form = UserForm(request.form)
		if user_form.validate():
			new_user = User(request.form['first_name'], request.form['last_name'])
			db.session.add(new_user)
			db.session.commit()
			return redirect(url_for('users.index'))
	return render_template('index.html', users=User.query.order_by(User.id).all())

@users_blueprint.route('/new')
def new():
	user_form=UserForm()
	return render_template('new.html', form=user_form)

@users_blueprint.route('/<int:id>', methods = ['GET', 'PATCH', 'DELETE'])
def show(id):
	user=User.query.get(id)
	if request.method == b'PATCH':
		user_form = UserForm(request.form)
		if user_form.validate():
			user.first_name = request.form['first_name']
			user.last_name = request.form['last_name']
			db.session.add(user)
			db.session.commit()
			return redirect(url_for('user.show'))
		else:
			return render_template('edit.html', form=user_form, user=user)
	elif request.method == b'DELETE':
		db.session.delete(user)
		db.session.commit()
		return redirect(url_for('user.index'))			
	return render_template('show.html', user=user)

@users_blueprint.route('/<int:id>/edit')
def edit(id):
	user=User.query.get(id)
	user_form=UserForm()
	return render_template('edit.html', form=user_form, user=user)


