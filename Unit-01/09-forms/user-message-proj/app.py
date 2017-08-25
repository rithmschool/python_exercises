##user-messages env

from flask import Flask,render_template,url_for,request,redirect,flash
from flask_modus import Modus 
from flask_sqlalchemy import SQLAlchemy 
import os
from forms import NewUserForm,NewMessageForm,EditUserForm,EditMessageForm

app = Flask(__name__)
modus = Modus(app)
if os.environ.get('ENV') == 'production':
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Message(db.Model):
	__tablename__ = "messages"

	id=db.Column(db.Integer,primary_key=True)
	text=db.Column(db.Text) ##limit text field to 50 chars?
	user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

	def __init__(self,user_id,text):
		self.user_id = user_id
		self.text = text

	def __repr__(self):
		return "The text of this message is {}".format(self.text)

class User(db.Model):
	__tablename__ = "users"

	id= db.Column(db.Integer,primary_key=True)
	username= db.Column(db.Text)
	email= db.Column(db.Text)
	first_name= db.Column(db.Text)
	last_name= db.Column(db.Text)
	messages = db.relationship('Message',backref='user',lazy='dynamic')

	def __init__(self,username,email,first_name,last_name):
		self.username = username
		self.email = email
		self.first_name = first_name
		self.last_name = last_name

	def __repr__(self):
		return "The username of this user is {}".format(self.username)

@app.route('/')
def root():
	return redirect(url_for('index'))

@app.route('/users',methods=['GET','POST'])
def index():
	form = NewUserForm(request.form)
	
	if request.method == "POST":
		if form.validate():
			flash('You have successfully added a new user!')
			new_user = User(form.name.data)
			db.session.add(new_user)
			db.session.commit()
			return redirect(url_for('index'))
		else:
			flash('The user must have a name, please try again.')
			render_template('users/new.html',form=form)


	return render_template('users/index.html',found_users=User.query.all())

@app.route('/users/new')
def new():
	form = NewUserForm(request.form)
	return render_template('users/new.html',form=form)

@app.route('/users/<id>',methods=["GET","PATCH","DELETE"])
def show(id): 
	found_user = User.query.get(id)
	form = EditUserForm(request.form)

	if request.method == b"PATCH":  
		if form.validate():
			flash('You have successfully edited the user!')
			found_user.name = form.data.get('name')
			db.session.add(found_user)
			db.session.commit()
			return redirect(url_for('index'))
		else:
			flash('You must have at least 1 letter in the edited user.')
			render_template('users/show.html',form=form,user=found_user)

	if request.method == b'DELETE':
		if form.validate():
			flash('You have succesfully deleted the user!')
			db.session.delete(found_user)
			db.session.commit()
			return redirect(url_for('index'))
		else:
			flash('You cannot delete this user.')
			render_template('users/show.html',form=form,user=found_user)

	return render_template('users/show.html',form=form,user=found_user)

@app.route('/users/<id>/edit',methods=['GET'])
def edit(id):
	found_user = User.query.get(id)
	form = EditUserForm(obj=found_user)
	return render_template('users/edit.html',user=found_user,form=form)

##messages

@app.route('/users/<int:user_id>/messages',methods=['GET','POST'])
def messages_index(user_id):
	form = NewMessageForm(request.form) ##form?
	if request.method == "POST":
		if form.validate():
			flash('You have successfully added a new message!')
			new_message = Message(form.title.data,user_id= user_id)
			db.session.add(new_message)
			db.session.commit()
			return redirect(url_for('messages_index',user_id=user_id))
		else: 
			flash('The message must have at least one letter in the title.')
			render_template('messages/new.html',user_id=user_id,form=form)
	
	user = User.query.get(user_id)
	return render_template('messages/index.html',user=user,user_id=user_id)


@app.route('/users/<int:user_id>/messages/new')
def messages_new(user_id):
	form = NewMessageForm(request.form)
	return render_template('messages/new.html',user_id=user_id,form=form)

@app.route('/users/<int:user_id>/messages/<int:message_id>',methods=["GET","PATCH","DELETE"])
def messages_show(user_id,message_id): 
	found_message = Message.query.get(message_id)
	form = EditMessageForm(request.form)
	
	if request.method == b"PATCH":
		if form.validate():
			flash('You have succesfully edited this message!')
			found_message.text = form.data.get('text')
			db.session.add(found_message)
			db.session.commit()
			return redirect(url_for('message_index',user_id=user_id))
		else:
			flash('You must have at least 1 letter in the edited message.')
			render_template('messages/show.html',form=form,user_id=user_id,found_message=found_message)

	if request.method == b'DELETE':
		if form.validate():
			flash('You have succesfully deleted this message!')
			db.session.delete(found_message)
			db.session.commit()
			return redirect(url_for('message_index',user_id=user_id))
		else:
			flash('You cannot delete this message.')
			render_template('messages/show.html',form=form,user_id=user_id,found_message=found_message)

	return render_template('messages/show.html',user_id=user_id,found_message=found_message)

@app.route('/users/<int:user_id>/messages/<int:message_id>/edit',methods=['GET'])
def messages_edit(user_id,message_id):
	found_message = Message.query.get(message_id)
	form = EditMessageForm(obj=found_message)
	return render_template('messages/edit.html',message_id=message_id,user_id=user_id,form=form)


if __name__ == '__main__':
	app.run(debug=True)


