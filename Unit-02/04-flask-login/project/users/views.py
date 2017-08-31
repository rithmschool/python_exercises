from flask import Blueprint, redirect, url_for, request, render_template, flash
from project.models import User
from project.users.forms import UserForm, SignupForm, LoginForm
from project import db
from flask_login import logout_user, login_user, current_user

from sqlalchemy.exc import IntegrityError

users_blueprint = Blueprint(
	'users',
	__name__,
	template_folder='templates'
)


@users_blueprint.route('/signup', methods=["GET","POST"])
def signup():
	signup_form=SignupForm(request.form)
	if request.method == "POST":
		if signup_form.validate():
			try:
				new_user=User(request.form.get('username'), request.form.get('email'), request.form.get('first_name'), request.form.get('last_name'), request.form.get('password'))
				db.session.add(new_user)
				db.session.commit()
			except IntegrityError as e:
				flash('Invalid submission.')
				return render_template('users/signup.html', signup_form=signup_form)
			flash('Successfully signed up!')
			return redirect(url_for('users.login'))
	return render_template('users/signup.html', signup_form=signup_form)

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
	login_form = LoginForm(request.form)
	if request.method == 'POST':
		if login_form.validate():
			user = User.authenticate(request.form.get('username'), request.form.get('password'))
			if user:
				login_user(user)
				flash("You successfully logged in!")
				return redirect(url_for('messages.index', user_id = user.id))
		flash('Invalid credentials.')
	return render_template('users/login.html', login_form=login_form)

@users_blueprint.route('/logout')
def logout():
	logout_user()
	flash('You have been signed out.')
	return redirect(url_for('messages'))



# @users_blueprint.route('/', methods=["GET", "POST"])
# def index():
# 	user_list = User.query.order_by(User.id).all()
# 	form = UserForm(request.form)
# 	if request.method == 'POST':
# 		if form.validate():
# 			try:
# 				new_user = User(request.form.get('username'), request.form.get('email'), request.form.get('first_name'), request.form.get('last_name'))
# 				db.session.add(new_user)
# 				db.session.commit()
# 			except IntegrityError as e:
# 				return render_template('new.html', form=form)
# 		flash('User Created!')
# 		return redirect(url_for('users.index'))
# 	if request.method == 'GET':
# 		return render_template('users/index.html', user_list = user_list)


# @users_blueprint.route('/new')
# def new():
# 	form = UserForm(request.form)
# 	return render_template('users/new.html', form = form)


# @users_blueprint.route('/<int:id>', methods=["GET", "PATCH", "DELETE"])
# def show(id):
# 	found_user = User.query.get_or_404(id)
# 	form = UserForm(request.form)
# 	if request.method == b"PATCH":
# 		if form.validate():
# 			found_user.username = request.form.get('username')
# 			found_user.email = request.form.get('email')
# 			found_user.first_name = request.form.get('first_name')
# 			found_user.last_name = request.form.get('last_name')
# 			db.session.add(found_user)
# 			db.session.commit()
# 			return redirect(url_for('users.index'))
# 		return render_template('users/edit.html', found_user=found_user, form=form)
# 	if request.method == b"DELETE":
# 		db.session.delete(found_user)
# 		db.session.commit()
# 		return redirect(url_for('users.index'))
# 	return render_template('users/show.html', found_user=found_user)


# @users_blueprint.route('/<int:id>/edit')
# def edit(id):
# 	found_user = User.query.get_or_404(id)
# 	form = UserForm(obj=found_user)
# 	return render_template('users/edit.html', found_user=found_user, form=form)

@users_blueprint.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')
