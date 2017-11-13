from flask import Blueprint, redirect, url_for, request, render_template, flash
from project.models import User
from project.users.forms import UserForm
from project import db

users_blueprint = Blueprint(
	'users',
	__name__,
	template_folder='templates'
)


@users_blueprint.route('/', methods=["GET", "POST"])
def index():
	user_list = User.query.order_by(User.id).all()
	form = UserForm(request.form)
	if request.method == 'POST':
		if form.validate():
			new_user = User(request.form.get('username'), request.form.get('email'), request.form.get('first_name'), request.form.get('last_name'))
			db.session.add(new_user)
			db.session.commit()
			flash('User Created!')
			return redirect(url_for('users.index'))
		return render_template('new.html', form=form)
	return render_template('users/index.html', user_list = user_list)


@users_blueprint.route('/new')
def new():
	form = UserForm(request.form)
	return render_template('users/new.html', form = form)


@users_blueprint.route('/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
	found_user = User.query.get_or_404(id)
	form = UserForm(request.form)
	if request.method == b"PATCH":
		if form.validate():
			found_user.username = request.form.get('username')
			found_user.email = request.form.get('email')
			found_user.first_name = request.form.get('first_name')
			found_user.last_name = request.form.get('last_name')
			db.session.add(found_user)
			db.session.commit()
			return redirect(url_for('users.index'))
		return render_template('users/edit.html', found_user=found_user, form=form)
	if request.method == b"DELETE":
		db.session.delete(found_user)
		db.session.commit()
		return redirect(url_for('users.index'))
	return render_template('users/show.html', found_user=found_user)


@users_blueprint.route('/<int:id>/edit')
def edit(id):
	found_user = User.query.get_or_404(id)
	form = UserForm(obj=found_user)
	return render_template('users/edit.html', found_user=found_user, form=form)

@users_blueprint.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')

