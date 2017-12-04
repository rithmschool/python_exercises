from project import db

class Message(db.Model):
	__tablename__= "messages"

	id=db.Column(db.Integer, primary_key=True)
	content = db.Column(db.Text)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __init__(self, content, user_id):
		self.content=content
		self.user_id=user_id