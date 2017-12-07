from project import db, bcrypt

class User(db.Model):

	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)
	username = db.Column(db.Text, unique=True)
	password = db.Column(db.Text)
	messages = db.relationship("Message", backref="user", lazy="dynamic", cascade="all, delete")

	def __init__(self, first_name, last_name, username, password):
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.password = bcrypt.generate_password_hash(password).decode('UTF-8')

	@classmethod
	def authenticate(clss, username, password):
		found = clss.query.filter_by(username=username).first()	
		if found:
			is_authenticated = bcrypt.check_password_hash(found.password, password)
			if is_authenticated:
				return found
		return False

class Message(db.Model):

	__tablename__ = "messages"

	id = db.Column(db.Integer, primary_key = True)
	text = db.Column(db.Text)
	img = db.Column(db.Text)
	user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

	def __init__(self, text, img, user_id):
		self.text = text
		self.img = img
		self.user_id = user_id
