from project import db

class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.Text)
	email = db.Column(db.Text)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)
	messages = db.relationship("Message", backref='user', cascade='delete', lazy='dynamic')


	def __init__(self,first_name,last_name,username,email):
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.email = email

