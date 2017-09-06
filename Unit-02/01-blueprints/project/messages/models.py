from project import db

class Message(db.Model):
	__tablename__ = "messages"

	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(120))
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __init__(self, text, user_id):
		self.text = text;
		self.user_id = user_id;

	def __repr__(self):
		return "Message is {}".format(self.text)