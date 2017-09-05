from project import db

class User(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.Text)
	email = db.Column(db.Text)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)
	messages = db.relationship('Message', backref='user', lazy='dynamic')

	def __init__(self, username, email, first_name, last_name):
		self.username = username
		self.email = email
		self.first_name = first_name
		self.last_name = last_name

	def __repr__(self):
		return "Username: {} / Email: {} / First & Last Names: {} {}".format(self.username, self.email, self.first_name, self.last_name)

MessageTag = db.Table('message_tags', 
	db.Column('id', db.Integer, primary_key=True), 
	db.Column('message_id', db.Integer, db.ForeignKey('messages.id', ondelete="cascade")),
	db.Column('tag_id', db.Integer, db.ForeignKey('tags.id', ondelete="cascade")))

class Message(db.Model):
	__tablename__ = "messages"
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.VARCHAR(100))
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	tags = db.relationship("Tag", secondary=MessageTag, backref=db.backref('messages'))

	def __init__(self, text, user_id):
		self.text = text
		self.user_id = user_id

class Tag(db.Model):
	__tablename__ = "tags"
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.Text)

	def __init__(self, text):
		self.text = text