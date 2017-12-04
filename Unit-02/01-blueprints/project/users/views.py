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
	delete_form=DeleteForm()
	if request.method == 'POST':
		user_form = UserForm(request.form)
		if user_form.validate():
			new_user = User(user_form.data['first_name'], user_form.data['last_name'])
			db.session.add(new_user)
			db.session.commit()
			return redirect(url_for('users.index'))
		return render_template('new.html', form=user_form)	
	return render_template('index.html', users=User.query.order_by(User.id).all(), delete_form=delete_form)

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
			user.first_name = user_form.data['first_name']
			user.last_name = user_form.data['last_name']
			db.session.add(user)
			db.session.commit()
			return redirect(url_for('users.index'))
		else:
			return render_template('edit.html', form=user_form, user=user)
	elif request.method == b'DELETE':
		delete_form = DeleteForm(request.form)
		if delete_form.validate():
			db.session.delete(user)
			db.session.commit()
			return redirect(url_for('users.index'))
		else:
			return "error"				
	return redirect(url_for('messages.index', user_id=id))

@users_blueprint.route('/<int:id>/edit')
def edit(id):
	user=User.query.get(id)
	user_form=UserForm(obj=user)
	return render_template('edit.html', form=user_form, user=user)


