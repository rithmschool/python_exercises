from project import db

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