from project import db, bcrypt
from flask_login import UserMixin

class User(db.Model, UserMixin):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.Text, unique=True)
	password = db.Column(db.Text)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)
	email = db.Column(db.Text)
	is_admin = db.Column(db.Boolean, default=False)
	messages = db.relationship('Message', backref='user', lazy='dynamic')

	def __init__(self, username, password, first_name, last_name, email):
		self.username = username;
		self.password = bcrypt.generate_password_hash(password).decode('UTF-8')
		self.first_name = first_name;
		self.last_name = last_name;
		self.email = email;

	def __repr__(self):
		return "User name is {}".format(self.username)


	@classmethod
	def authenticate(cls, username, password):
		found_user = cls.query.filter_by(username = username).first()
		if found_user:
			authenticated_user = bcrypt.check_password_hash(found_user.password, password)
			if authenticated_user:
				return found_user
		return False