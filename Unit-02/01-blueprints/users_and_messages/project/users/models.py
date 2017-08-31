from project import db
from project.messages.models import Message

# Class(es) ------------------------------------------------
class User(db.Model):

	__tablename__ = "users"

	# Create the columns for our users table
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.Text)
	email = db.Column(db.Text)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)
	# Adding the code below to enable a relationship with the messages table
	messages = db.relationship('Message', backref='user', lazy='dynamic')

	# Define what each intance/row in the DB will have 
	def __init__(self, username, email, first_name, last_name):
		self.username = username
		self.email = email
		self.first_name = first_name
		self.last_name = last_name

	# Include a repr to see additional information about each instance
	def __repr__(self):
		return "User username: {}, email: {}, first_name: {}, last_name: {}".format(self.username, self.email, self.first_name, self.last_name)





