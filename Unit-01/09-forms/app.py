from flask import Flask, render_template, redirect, url_for, request, abort, flash
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
from forms import UserForm, MessageForm, Edit_UserForm, Edit_MessageForm
import os

app = Flask(__name__)
modus = Modus(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/flask-user-messages'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

class User(db.Model):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.Text)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)
	email = db.Column(db.Text)
	messages = db.relationship('Message', backref='user', lazy='dynamic')

	def __init__(self, username, first_name, last_name, email):
		self.username = username;
		self.first_name = first_name;
		self.last_name = last_name;
		self.email = email;

	def __repr__(self):
		return "User name is {}".format(self.username)

class Message(db.Model):
	__tablename__ = "messages"

	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(120))
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __init__(self, text, user_id):
		self.text = text;
		self.user_id = user_id;

	def __repr__(self):
		return "Message is {}".format(self.text)

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/users', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		form = UserForm(request.form)
		if form.validate():
			n_user = User(request.form.get('username'), request.form.get('first_name'),
			 request.form.get('last_name'), request.form.get('email'))
			db.session.add(n_user)
			db.session.commit()
			flash("You have successfully added a User!")
			return redirect(url_for('index'))
		else:
			return render_template('users/new.html', form=form)

	u_list = User.query.order_by(User.username).all()
		
	return render_template('users/index.html', users=u_list)

@app.route('/users/new')
def new():
	form = UserForm(request.form)
	return render_template('users/new.html', form=form)

@app.route('/users/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):
	found_user = User.query.filter_by(id=id).first()

	if found_user is None:
		abort(404)

	if request.method == b"DELETE":
		db.session.delete(found_user)
		db.session.commit()
		flash("You have successfully deleted User {}".format(found_user.username))
		return redirect(url_for('index'))

	if request.method == b"PATCH":
		form = Edit_UserForm(request.form)
		if form.validate():
			found_user.username = request.form.get('username')
			found_user.first_name = request.form.get('first_name')
			found_user.last_name = request.form.get('last_name')
			found_user.email = request.form.get('email')
			db.session.add(found_user)
			db.session.commit()
			flash("You have successfully updated a User!")
			return redirect(url_for('index'))
		else:
			return render_template('users/edit.html', user=found_user, form=form)

	return render_template('users/show.html', user=found_user)

@app.route('/users/<int:user_id>/messages', methods=['GET', 'POST'])
def messages_index(user_id):
	found_user = User.query.filter_by(id=user_id).first()

	if request.method == "POST":
		form = MessageForm(request.form)
		if form.validate():
			n_message = Message(request.form.get('text'), found_user.id)
			db.session.add(n_message)
			db.session.commit()
			flash("You have successfully added a Message!")
			return redirect(url_for('messages_index', user_id=found_user.id))
		else:
			return render_template('messages/new.html', user_id=found_user.id, form=form)
		
	return render_template('messages/index.html', user=found_user)

@app.route('/users/<int:user_id>/messages/new')
def messages_new(user_id):
	form = MessageForm(request.form)
	return render_template('messages/new.html', user_id=user_id, form=form)

@app.route('/users/<int:user_id>/messages/<int:id>', methods=['GET', 'POST',
 'PATCH', 'DELETE'])
def messages_show(user_id, id):
	found_message = Message.query.filter_by(id=id).first()

	if found_message is None:
		abort(404)

	if request.method == b"DELETE":
		db.session.delete(found_message)
		db.session.commit()
		flash("You have successfully deleted Message {}".format(found_message.text))
		return redirect(url_for('messages_index', user_id=found_message.user_id))

	if request.method == b"PATCH":
		form = Edit_MessageForm(request.form)
		if form.validate():
			found_message.text = request.form.get('text')
			db.session.add(found_message)
			db.session.commit()
			flash("You have successfully updated a Message!")
			return redirect(url_for('messages_index', user_id=found_message.user_id))
		else:
			return render_template('messages/edit.html', message=found_message, form=form)

	return render_template('messages/show.html', message=found_message)

@app.route('/users/<int:id>/edit', methods=['GET'])
def edit(id):
	found_user = User.query.filter_by(id=id).first()
	form = Edit_UserForm(obj=found_user)

	if found_user is None:
		abort(404)

	return render_template('users/edit.html', user=found_user, form=form)

@app.route('/users/<int:user_id>/messages/<int:id>/edit', methods=['GET'])
def messages_edit(user_id, id):
	found_message = Message.query.filter_by(id=id).first()
	form = Edit_MessageForm(obj=found_message)

	if found_message is None:
		abort(404)

	return render_template('messages/edit.html', message=found_message, form=form)

if __name__ == '__main__':
    app.run(debug=True,port=3000)