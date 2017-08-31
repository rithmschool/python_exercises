from flask import redirect, render_template, request, url_for, Blueprint
from project.users.models import User
from project.users.forms import UserForm 
from project import db

users_blueprint = Blueprint(
	'users',
	__name__,
	template_folder='templates'
)

# Route(es) ------------------------------------------------

# # User routes -------------------
# # Multi purpose page - it's the default page (where you can see a list of all users), and also 
# # where the POST method logic is handled for creating a new user
@users_blueprint.route('/', methods=["GET", "POST"])
def index():

# 	# This code handles POST request from new.html - adds a new user and redirects to index.html
	if request.method == "POST":
		form = UserForm()
		if form.validate():
			new_user = User(request.form['username'], request.form['email'], request.form['first_name'], request.form['last_name'])
			db.session.add(new_user)
			db.session.commit()
			return redirect(url_for('users.index'))
		return render_template('users/new.html', form=form)
	return render_template('users/index.html', users=User.query.all())

# # Render template - displays form with blank fields (info that will be used to create a new user)
@users_blueprint.route('/new')
def new():
	form = UserForm()
	return render_template('users/new.html', form=form)

@users_blueprint.route('/<int:id>/edit')
def edit(id):
# The id in the url can be used as a query argument	
	user = User.query.get(id)
	form = UserForm(obj=user)
	return render_template('users/edit.html', form=form, user=user) 

# Render template  - displays current info on a specific user 
@users_blueprint.route('/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
# The id in the url can be used as a query argument

	found_user = User.query.get(id)

	if request.method == b"PATCH":
		form = UserForm(request.form)
		if form.validate():
			found_user.username = request.form['username']
			found_user.email = request.form['email']
			found_user.first_name = request.form['first_name']
			found_user.last_name = request.form['last_name']
			db.session.add(found_user)
			db.session.commit()
			return redirect(url_for('users.index'))
		return render_template('users/edit.html', form=form, user=found_user)

	if request.method == b"DELETE":
		db.session.delete(found_user)
		db.session.commit()
		return redirect(url_for('users.index'))		

	return render_template('users/show.html', user=found_user)

# Render form - displays current info on a specific user, and user details can be edited or user can be 
# deleted entirely.  Route has update and delete buttons on page - logic for these buttons is handled
# on the show page. 









