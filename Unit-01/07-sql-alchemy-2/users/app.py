# we will need users
# users can have many messages
# need a 1 to many relationship in the DB
# create users, create relationship with messages
# create CRUD operations for users and messages
# create a form for each using WTForms
# which will need environment variables to prevent CSRF attacks
# deploy to heroku: need to do conditional logic for dev vs. prod envs

from flask import Flask, redirect, render_template, url_for, flash, request
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
from forms import AddUserForm, AddMessageForm
import os

app = Flask(__name__)
modus = Modus(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/flask-users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)

class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.Text)
	email = db.Column(db.Text)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)
	messages = db.relationship('Message', backref='user', lazy='dynamic')

	def __init__(self, username, email, first_name, last_name):
		self.username = username
		self.email = email
		self.first_name = first_name
		self.last_name = last_name

	def __repr__(self):
		return "Username: {} / Email: {} / First & Last Names: {} {}".format(self.username, self.email, self.first_name, self.last_name)

class Message(db.Model):
	__tablename__ = "messages"
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.VARCHAR(100))
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __init__(self, text, user_id):
		self.text = text
		self.user_id = user_id

@app.route('/')
def root():
	return redirect(url_for('index_users'))

@app.route('/users')
def index_users():
	return render_template('users/index.html', users=User.query.all())

@app.route('/users/new', methods=['GET', 'POST'])
def new_user():
	form = AddUserForm(request.form)
	if request.method == "POST":
		if form.validate():
			created_user = User(form.username.data, form.email.data, form.first_name.data, form.last_name.data)
			db.session.add(created_user)
			db.session.commit()
			flash("You have successfully created a new user!")
			return redirect(url_for('index_users'))
		return render_template('users/new.html', form=form)
	return render_template('users/new.html', form=form)

@app.route('/users/<int:user_id>', methods=['GET', 'PATCH', 'DELETE'])
def show_user(user_id):
	user = User.query.get(user_id)
	form = AddUserForm(request.form)
	if request.method == b"PATCH":
		if form.validate():
			user.username = form.username.data
			user.email = form.email.data
			user.first_name = form.first_name.data
			user.last_name = form.last_name.data
			db.session.add(user)
			db.session.commit()
			flash("You have successfully edited this user.")
			return redirect(url_for('index_users'))
		flash("Please enter proper values for each field.")
		return redirect(url_for('edit_user', user_id=user.id, form=form))
	if request.method == b"DELETE":
		db.session.delete(user)
		db.session.commit()
		flash("You've successfully deleted {}".format(user.username))
		return redirect(url_for('index_users'))
	return redirect(url_for('edit_user', user_id=user.id, form=form))

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
	user = User.query.get(user_id)
	form = AddUserForm(request.form)
	return render_template('users/edit.html', user=user, form=form)

@app.route('/users/<int:user_id>/messages')
def index_messages(user_id):
	user = User.query.get(user_id)
	return render_template('messages/index.html', user=user)

@app.route('/users/<int:user_id>/messages/new', methods=['GET', 'POST'])
def new_message(user_id):
	form = AddMessageForm(request.form)
	user = User.query.get(user_id)
	if request.method == "POST":
		if form.validate():
			created_msg = Message(form.text.data, user.id)
			db.session.add(created_msg)
			db.session.commit()
			flash("You have successfully added a new message!")
			return redirect(url_for('index_messages', user_id=user.id))
		flash("Please enter valid text.")
		return redirect(url_for('new_message', user_id=user.id, form=form))
	return render_template('messages/new.html', user=user, form=form)

@app.route('/users/<int:user_id>/messages/<int:message_id>', methods=['GET', 'PATCH', 'DELETE'])
def show_message(user_id, message_id):
	user = User.query.get(user_id)
	message = Message.query.get(message_id)
	form = AddMessageForm(request.form)
	if request.method == b"PATCH":
		if form.validate():
			message.text = form.text.data
			db.session.add(message)
			db.session.commit()
			flash("You have successfully edited this message.")
			return redirect(url_for('index_messages', user_id=user.id))
		flash("Please enter proper values.")
		return redirect(url_for('edit_message', user_id=user.id, message_id=message.id, form=form))
	if request.method == b"DELETE":
		db.session.delete(message)
		db.session.commit()
		flash("You've successfully deleted {}'s message.".format(user.username))
		return redirect(url_for('index_messages', user_id=user.id))
	return render_template('messages/edit.html', user_id=user.id, message_id=message.id)

@app.route('/users/<int:user_id>/messages/<int:message_id>/edit')
def edit_message(user_id, message_id):
	user = User.query.get(user_id)
	message = Message.query.get(message_id)
	form = AddMessageForm(request.form)
	return render_template('messages/edit.html', user=user, message=message, form=form)

if __name__ == "__main__":
	app.run(debug=True,port=3000)