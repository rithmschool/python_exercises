from flask import redirect, render_template, request, url_for, Blueprint, abort, flash
from project.users.models import User
from project.users.forms import UserForm, EditUserForm, DeleteUserForm
from project import db

users_blueprint = Blueprint(
	'users',
	__name__,
	template_folder='templates'
)

@users_blueprint.route('/', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		form = UserForm(request.form)
		if form.validate():
			n_user = User(request.form.get('username'), request.form.get('first_name'),
			 request.form.get('last_name'), request.form.get('email'))
			db.session.add(n_user)
			db.session.commit()
			flash("You have successfully added a User!")
			return redirect(url_for('users.index'))
		else:
			return render_template('users/new.html', form=form)
		
	return render_template('users/index.html', users=User.query.order_by(User.username).all())

@users_blueprint.route('/new')
def new():
	form = UserForm(request.form)
	return render_template('users/new.html', form=form)

@users_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
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
			return redirect(url_for('users.index'))
		else:
			d_form = DeleteUserForm()
			return render_template('users/edit.html', user=found_user, d_form=d_form, e_form=e_form)

	return render_template('users/show.html', user=found_user)

@users_blueprint.route('/<int:id>/edit', methods=['GET'])
def edit(id):
	found_user = User.query.filter_by(id=id).first()
	e_form = EditUserForm(obj=found_user)
	d_form = DeleteUserForm()

	if found_user is None:
		abort(404)

	return render_template('users/edit.html', user=found_user, e_form=e_form, d_form=d_form)