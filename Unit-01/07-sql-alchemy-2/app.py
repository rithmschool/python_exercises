from flask import Flask, url_for, redirect, render_template, request
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
from forms import UserForm, MessageForm, DeleteForm
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/user'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
modus = Modus(app)
db = SQLAlchemy(app)

class User(db.Model):

	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)
	messages = db.relationship("Message", backref="user", lazy="dynamic", cascade="all, delete")

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

class Message(db.Model):

	__tablename__ = "messages"

	id = db.Column(db.Integer, primary_key = True)
	text = db.Column(db.Text)
	img = db.Column(db.Text)
	user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

	def __init__(self, text, img, user_id):
		self.text = text
		self.img = img
		self.user_id = user_id

# USERS SECTION
@app.route("/")
def root():
	return redirect(url_for('index'))

@app.route("/users", methods = ["GET", "POST"])
def index():
	if request.method == "POST":
		form = UserForm(request.form)
		if form.validate():
			user = User(form.first_name.data, form.last_name.data)
			db.session.add(user)
			db.session.commit()
			return redirect(url_for('index'))
		return render_template('users/new.html', form=form)	
	users = User.query.all() 
	return render_template('users/index.html', users=users)

@app.route("/users/new")
def new():
	form = UserForm()
	return render_template('users/new.html', form=form)

@app.route("/users/<int:id>", methods = ["GET", "PATCH", "DELETE"])
def show(id):
	user = User.query.get(id)
	if request.method == b"PATCH":
		form = UserForm(request.form)
		if form.validate():
			user.first_name = form.first_name.data
			user.last_name = form.last_name.data
			db.session.add(user)
			db.session.commit()
			return redirect(url_for('index'))
		return render_template('users/edit.html', user=user, form=form)
	if request.method == b"DELETE":
		delete_form = DeleteForm(request.form)
		if delete_form.validate():
			db.session.delete(user)
			db.session.commit()
		return redirect(url_for('index'))
	delete_form = DeleteForm()
	return render_template('users/show.html', user=user, delete_form=delete_form)

@app.route("/users/<int:id>/edit")
def edit(id):
	user = User.query.get(id)
	form = UserForm(obj=user)
	return render_template('users/edit.html', user=user, form=form)

#USERS/MESSAGES SECTION
@app.route("/users/<int:user_id>/messages", methods = ["GET", "POST"])
def m_index(user_id):
	if request.method == "POST":
		message = Message(request.form.get("text"), request.form.get("img"), user_id)
		db.session.add(message)
		db.session.commit()
		return redirect(url_for('m_index', user_id=user_id))
	user = User.query.get(user_id)
	return render_template('messages/index.html', user=user)

@app.route("/users/<int:user_id>/messages/new")
def m_new(user_id):
	form = MessageForm()
	user = User.query.get(user_id)
	return render_template('messages/new.html', user=user, form=form)

@app.route("/users/<int:user_id>/messages/<int:id>", methods = ["GET", "PATCH", "DELETE"])
def m_show(user_id, id):
	message = Message.query.get(id)
	if request.method == b"PATCH":
		form = MessageForm(request.form)
		if form.validate():
			message.text = form.text.data
			message.img = form.img.data
			db.session.add(message)
			db.session.commit()
			return redirect(url_for('m_index', user_id=user_id))
		return render_template('messages/edit.html', message=message, form=form)
	if request.method == b"DELETE":
		delete_form = DeleteForm(request.form)
		if delete_form.validate():
			db.session.delete(message)
			db.session.commit()
		return redirect(url_for('m_index', user_id=user_id))
	delete_form = DeleteForm()
	return render_template('messages/show.html', message=message, delete_form=delete_form)

@app.route("/users/<int:user_id>/messages/<int:id>/edit")
def m_edit(user_id, id):
	message = Message.query.get(id)
	form = MessageForm(obj=message)
	return render_template('messages/edit.html', message=message, form=form)

if __name__ == '__main__':
  app.run(debug=True)

