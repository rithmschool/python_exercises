from flask import Flask, url_for, redirect, render_template, request
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/user'#user
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
modus = Modus(app)#we don't use this either
db = SQLAlchemy(app)#we use this

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

	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key = True)
	text = db.Column(db.Text)
	img = db.Column(db.Text)
	user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name


@app.route("/")
def root():
	return redirect(url_for('index'))

@app.route("/users", methods = ["GET", "POST"])
def index():
	if request.method == "POST":
		user = User(request.form.get("first_name"),request.form.get("last_name"))
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('index'))
	users = User.query.all()
	return render_template('index.html', users = users)

@app.route("/users/new")
def new():
	return render_template('new.html')

@app.route("/users/<int:id>", methods = ["GET", "PATCH", "DELETE"])
def show(id):
	user = User.query.get(id)
	if request.method == b"PATCH":
		user.first_name = request.form.get("first_name")
		user.last_name = request.form.get("last_name")
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('index'))
	if request.method == b"DELETE":
		db.session.delete(user)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('show.html', user = user)

@app.route("/users/<int:id>/edit")
def edit(id):
	user = User.query.get(id)
	return render_template('m_edit.html', user = user)

@app.route("/users/<int:user_id>/messages", methods = ["GET", "POST"])
def m_index(user_id):
	if request.method == "POST":
		message = Message(request.form.get("text"), request.form.get("img"))
		db.session.add(message)
		db.session.commit()
		return redirect(url_for('m_index'), user_id = user_id)
	user = User.query.get(user_id)
	return render_template('m_index.html', user = user)

@app.route("/users/<int:user_id>/messages/new")
def m_new(user_id):
	user = User.query.get(user_id)
	return render_template('m_new.html', user = user)

@app.route("/users/<int:user_id>/messages/<int:id>", methods = ["GET", "PATCH", "DELETE"])
def m_show(user_id, id):
	message = Message.query.get(id)
	if request.method == b"PATCH":
		message.text = request.form.get("text") 
		message.img = request.form.get("img")
		db.session.add(message)
		db.session.commit()
		return redirect(url_for('m_index'), user_id = user_id)
	if request.method == b"DELETE":
		db.session.delete(message)
		return redirect(url_for('m_index'), user_id = user_id)
	user = User.query.get(user_id)	
	return render_template('m_show.html', user = user)

@app.route("/users/<int:user_id>/messages/<int:id>/edit")
def m_edit(user_id, id):
	message = Message.query.get(id)
	return render_template('m_edit.html', message = message)



