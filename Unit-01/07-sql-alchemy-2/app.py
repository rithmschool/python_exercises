from flask import Flask, request, url_for, redirect, render_template
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/users-messages-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
modus = Modus(app)

class User(db.Model):

	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.Text)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)
	messages = db.relationship('Message', backref = 'user', lazy='dynamic', cascade='all,delete')

	def __init__(self, username, first_name, last_name):
		self.username = username
		self.first_name = first_name
		self.last_name = last_name
	
	def __repr__(self):
		return "{}'s name is {} {}.".format(self.username, self.first_name, self.last_name)

class Message(db.Model):

	__tablename__ = 'messages'

	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.Text)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __init__(self, text, user_id):
		self.text = text
		self.user_id = user_id

@app.route('/')
def root():
	return redirect(url_for('index'))

@app.route('/users', methods=['POST', 'GET'])
def index():
	if request.method=='POST':
		new_user = User(request.form['username'],request.form['first_name'],request.form['last_name'])
		db.session.add(new_user)
		db.session.commit()
		return redirect(url_for('index'))	
	return render_template('users/index.html', users=User.query.all())

@app.route('/users/new')
def new():
	return render_template('users/new.html')

@app.route('/users/<int:id>', methods=['GET','PATCH','DELETE'])
def show(id):
	found_user = User.query.get(id)
	if request.method == b'PATCH':
		found_user.username = request.form['username']
		found_user.first_name = request.form['first_name']
		found_user.last_name = request.form['last_name']
		db.session.add(found_user)
		db.session.commit()
		return redirect(url_for('index'))
	if request.method ==b'DELETE':
		db.session.delete(found_user)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('users/show.html', user=found_user)

@app.route('/users/<int:id>/edit')
def edit(id):
	return render_template('users/edit.html', user=User.query.get(id))

@app.route('/users/<int:user_id>/messages', methods = ['GET', 'POST'])
def messages_index(user_id):
	if request.method == "POST":
		new_message = Message(request.form['text'], user_id)
		db.session.add(new_message)
		db.session.commit()
		return redirect(url_for('messages_index', user_id = user_id))
	user = User.query.get(user_id)	
	return render_template('messages/index.html', user=user)
		
@app.route('/users/<int:user_id>/messages/new')
def messages_new(user_id):
	found_user = User.query.get(user_id)
	return render_template('messages/new.html', user= found_user)

@app.route('/users/<int:user_id>/messages/<int:id>', methods=['PATCH', 'GET', 'DELETE'])
def messages_show(user_id, id):
	found_message = Message.query.get(id)
	if request.method == b'PATCH':
		found_message.text = request.form['text']
		db.session.add(found_message)
		db.session.commit()
		return redirect(url_for('messages_index', user_id = user_id))
	if request.method == b'DELETE':
		db.session.delete(found_message)
		db.session.commit()
		return redirect(url_for('messages_index', user_id=user_id))
	return render_template('messages/show.html', message = found_message)	

@app.route('/users/<int:user_id>/messages/<int:id>/edit')
def messages_edit(user_id, id):
	found_message = Message.query.get(id)
	return render_template('messages/edit.html', message=found_message)

if __name__ == '__main__':
	app.run(debug=True)	