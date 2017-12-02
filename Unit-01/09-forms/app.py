from flask import Flask, request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy 
from flask_modus import Modus 
from forms import UserForm, MessageForm, DeleteForm
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/users-messages'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
modus=Modus(app)
db=SQLAlchemy(app)

class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)
	messages = db.relationship('Message', backref='user', lazy='dynamic', cascade="all,delete")

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

class Message(db.Model):
	__tablename__ = 'messages'
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.Text)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __init__(self, content, user_id):
		self.content = content
		self.user_id = user_id


@app.route('/')
def root():
	return redirect(url_for('index'))

@app.route('/users', methods = ['GET', 'POST'])
def index():
	delete_form = DeleteForm()
	if request.method == "POST":
		form = UserForm(request.form)
		if form.validate():
			new_user = User(request.form.get('first_name'), request.form.get('last_name'))
			db.session.add(new_user)
			db.session.commit()
			return redirect(url_for('index'))
		else:
			return render_template('users/new.html', form = form)
	return render_template('users/index.html', users = User.query.all(), delete_form = delete_form)

@app.route('/users/new')
def new():
	user_form = UserForm()
	return render_template('users/new.html', form = user_form)

@app.route('/users/<int:id>/edit')
def edit(id):
	found_user = User.query.get(id)
	user_form = UserForm(obj=found_user)
	return render_template('users/edit.html', user = found_user, form =user_form)

@app.route('/users/<int:id>', methods = ['GET', 'PATCH', 'DELETE'])
def show(id):
	found_user = User.query.get(id)
	if request.method == b'PATCH':
		form = UserForm(request.form)
		if form.validate():
			found_user.first_name = form.first_name.data
			found_user.last_name = form.last_name.data
			db.session.add(found_user)
			db.session.commit()
			return redirect(url_for('show', id=id))
		else:
			return render_template('users/edit.html', user = found_user, form =form)
	if request.method == b'DELETE':
		delete_form = DeleteForm(request.form)
		if delete_form.validate():
			db.session.delete(found_user)
			db.session.commit()
		return redirect(url_for('index'))
	return render_template('users/show.html', user = User.query.get(id))

# Messages
@app.route('/users/<int:user_id>/messages', methods = ["GET", "POST"])
def messages_index(user_id):
	delete_form = DeleteForm()
	if request.method == 'POST':
		form = MessageForm(request.form)
		if form.validate():
			new_message = Message(request.form.get('content'), user_id)
			db.session.add(new_message)
			db.session.commit()
			return redirect(url_for('messages_index', user_id = user_id))
		else:
			return render_template('messages/new.html', user = User.query.get(user_id), form = form)
	return render_template('messages/index.html', user=User.query.get(user_id), delete_form=delete_form)

@app.route('/users/<int:user_id>/messages/new')
def messages_new(user_id):
	message_form = MessageForm()
	# pass in the user here cause need it for the post request
	return render_template('messages/new.html', user = User.query.get(user_id), form = message_form)

@app.route('/users/<int:user_id>/messages/<int:id>/edit')
def messages_edit(user_id, id):
	found_message = Message.query.get(id)
	message_form = MessageForm(obj=found_message)
	return render_template('messages/edit.html', message = found_message, form=message_form)

@app.route('/users/<int:user_id>/messages/<int:id>', methods = ["GET", "PATCH", "DELETE"])
def messages_show(user_id, id):
	found_message = Message.query.get(id)
	if request.method == b'PATCH':
		form = MessageForm(request.form)
		if form.validate():
			found_message.content = request.form.get('content')
			db.session.add(found_message)
			db.session.commit()
			return redirect(url_for('messages_index', user_id = user_id))
		else:
			return render_template('messages/edit.html', message = found_message, form=form)
	if request.method == b'DELETE':
		delete_form = DeleteForm(request.form)
		if delete_form.validate():
			db.session.delete(found_message)
			db.session.commit()
		return redirect(url_for('messages_index', user_id = user_id))
	return render_template('messages/show.html', message=found_message)

if __name__ == '__main__':
	app.run(debug=True, port=3000)