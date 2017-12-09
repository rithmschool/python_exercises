from flask import redirect, render_template, request, url_for, Blueprint, flash
from project.users.models import User
from project.users.forms import UserForm, DeleteForm, LoginForm
from project import db, bcrypt
from sqlalchemy.exc import IntegrityError
from project.decorators import prevent_login_signup, ensure_correct_user
from flask_login import login_user, logout_user, login_required

users_blueprint = Blueprint(
	'users',
	__name__,
	template_folder = 'templates'
)


@users_blueprint.route('/')
@login_required
def index():
	delete_form = DeleteForm()
	return render_template('users/index.html', users = User.query.all(), delete_form = delete_form)

@users_blueprint.route('/', methods = ['POST'])
@prevent_login_signup
def signup():
	form = UserForm(request.form)
	if form.validate():
		try:
			new_user = User(form.first_name.data, 
				form.last_name.data, 
				form.username.data,
				form.password.data,
				form.profile_link.data)
			db.session.add(new_user)
			db.session.commit()
			login_user(new_user)
			flash('User Created!')
			return redirect(url_for('users.index'))
		except IntegrityError as e:
			flash('Username already taken')
			return render_template('users/new.html', form = form)
	
	return render_template('users/new.html', form = form)
	

@users_blueprint.route('/login', methods = ["GET", "POST"])
@prevent_login_signup
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        authenticated_user = User.authenticate(form.username.data, form.password.data)
        if authenticated_user:
            login_user(authenticated_user)
            flash("You are now logged in!")
            return redirect(url_for('users.index'))
        else:
            flash("Invalid Credentials")
            return redirect(url_for('users.login'))
    return render_template('users/login.html', form=form)


@users_blueprint.route('/new')
@prevent_login_signup
def new():
	user_form = UserForm()
	return render_template('users/new.html', form = user_form)

@users_blueprint.route('/<int:id>/edit')
@login_required
@ensure_correct_user
def edit(id):
	found_user = User.query.get_or_404(id)
	user_form = UserForm(obj=found_user)
	return render_template('users/edit.html', user = found_user, form =user_form)

@users_blueprint.route('/<int:id>', methods = ['GET', 'PATCH', 'DELETE'])
@login_required
@ensure_correct_user
def show(id):
	found_user = User.query.get_or_404(id)
	if request.method == b'PATCH':
		form = UserForm(request.form)
		if form.validate():
			found_user.first_name = form.first_name.data
			found_user.last_name = form.last_name.data
			found_user.profile_link = form.profile_link.data
			found_user.password = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
			db.session.add(found_user)
			db.session.commit()
			flash('User Updated!')
			return redirect(url_for('users.index'))
		else:
			return render_template('users/edit.html', user = found_user, form =form)
	if request.method == b'DELETE':
		delete_form = DeleteForm(request.form)
		if delete_form.validate():
			db.session.delete(found_user)
			db.session.commit()
			logout_user()
			flash('User Deleted!')
		return redirect(url_for('users.index'))
	return render_template('users/show.html', user = User.query.get(id))

@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged Out!')
    return redirect(url_for('users.login'))

