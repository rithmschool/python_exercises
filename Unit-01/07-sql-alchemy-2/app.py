from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy 
from flask_modus import Modus
from forms import UserForm, MessageForm
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/user-messages'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
modus = Modus(app)
app.config['SECRET_KEY']=os.environ.get('SECRET_KEY')

#============================================================================================================
# classes
#============================================================================================================

class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.Text)
	email = db.Column(db.Text)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)
	messages = db.relationship("Message", backref='user', cascade='delete', lazy='dynamic')


	def __init__(self,username,email,first_name,last_name):
		self.username = username
		self.email = email
		self.first_name = first_name
		self.last_name = last_name


class Message(db.Model):
	__tablename__ = 'messages'

	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.Text)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __init__(self,text,user_id):
		self.text = text
		self.user_id= user_id

#============================================================================================================
# Users
#============================================================================================================
@app.route('/')
def root():
	return redirect(url_for('index'))

@app.route('/users', methods=["GET", "POST"])
def index():
	user_list = User.query.order_by(User.id).all()
	form = UserForm(request.form)
	if request.method == 'POST':
		if form.validate():
			new_user = User(request.form.get('username'), request.form.get('email'), request.form.get('first_name'), request.form.get('last_name'))
			db.session.add(new_user)
			db.session.commit()
			flash('User Added')
			return redirect(url_for('index'))
		else:
			return render_template('new.html', form=form)
	return render_template('user/index.html', user_list = user_list)


@app.route('/users/new')
def new():
	form = UserForm(request.form)
	return render_template('user/new.html', form = form)


@app.route('/users/<int:id>', methods=["GET", "PATCH", "DELETE"])
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
			return redirect(url_for('index'))
		else:
			return render_template('user/edit.html', found_user=found_user, form=form)
	if request.method == b"DELETE":
		db.session.delete(found_user)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('user/show.html', found_user=found_user)


@app.route('/users/<int:id>/edit')
def edit(id):
	found_user = User.query.get_or_404(id)
	form = UserForm(obj=found_user)
	return render_template('user/edit.html', found_user=found_user, form=form)

#============================================================================================================
# Messages
#============================================================================================================

@app.route('/users/<int:user_id>/messages', methods=["GET", "POST"])
def message_index(user_id):
	found_user = User.query.get_or_404(user_id)
	form = MessageForm(request.form)
	if request.method == "POST":
		if form.validate():
			db.session.add(Message(request.form.get('text'), found_user.id))
			db.session.commit()
			return redirect(url_for('message_index', user_id = user_id))
		else:
			return render_template('message/new.html', found_user=found_user, form=form)
	message_list = found_user.messages.order_by(Message.id).all()
	return render_template('message/index.html', found_user=found_user, message_list=message_list)

@app.route('/users/<int:user_id>/messages/new')
def message_new(user_id):
	found_user = User.query.get_or_404(user_id)
	form = MessageForm(request.form)
	return render_template('message/new.html', found_user=found_user, form=form)

@app.route('/users/<int:user_id>/messages/<int:id>', methods=["GET", "PATCH", "DELETE"])
def message_show(user_id,id):
	found_user = User.query.get_or_404(user_id)
	found_message = Message.query.get_or_404(id)
	form = MessageForm(request.form)
	if request.method == b"PATCH":
		if form.validate():
			found_message.text = request.form.get('text')
			db.session.add(found_message)
			db.session.commit()
			return redirect(url_for('message_index', user_id=found_user.id))
		else:
			return render_template('message/edit.html', found_user=found_user, found_message=found_message, form=form)
	if request.method == b"DELETE":
		db.session.delete(found_message)
		db.session.commit()
		return redirect(url_for('message_index', user_id=found_user.id))
	return render_template('message/show.html', found_message=found_message, found_user = found_user)

@app.route('/users/<int:user_id>/messages/<int:id>/edit')
def message_edit(user_id,id):
	found_user = User.query.get_or_404(user_id)
	found_message = Message.query.get_or_404(id)
	form = MessageForm(obj=found_message)
	return render_template('message/edit.html', found_user=found_user, found_message = found_message, form=form)



#============================================================================================================
# 404 page
#============================================================================================================
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')

if __name__ == "__main__":
	app.run(port=3000, debug=True)