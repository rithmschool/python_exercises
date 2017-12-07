from project import db

MessageTag = db.Table('messages_tags',
		db.Column('id', db.Integer, primary_key =True),
		db.Column('messages_id', db.Integer, db.ForeignKey('messages.id', ondelete='cascade')),
		db.Column('tags_id', db.Integer, db.ForeignKey('tags.id', ondelete='cascade'))
	)

class Message(db.Model):

	__tablename__ = "messages"

	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.Text)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	tags = db.relationship('Tag', secondary= MessageTag, backref=db.backref('messages'))

	def __init__(self, content, user_id):
		self.content = content
		self.user_id = user_id

