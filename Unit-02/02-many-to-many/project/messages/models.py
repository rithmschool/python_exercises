from project import db
from project.tags.models import Tag

MessageTag = db.Table('message_tags',
                              db.Column('id',
                                        db.Integer,
                                        primary_key=True),
                              db.Column('message_id',
                                        db.Integer,
                                        db.ForeignKey('messages.id', ondelete="cascade")),
                              db.Column('tag_id',
                                        db.Integer,
                                        db.ForeignKey('tags.id', ondelete="cascade")))

class Message(db.Model):
	__tablename__ = "messages"

	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(120))
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	tags = db.relationship("Tag", secondary=MessageTag,
                                backref=db.backref('messages'))

	def __init__(self, text, user_id):
		self.text = text;
		self.user_id = user_id;

	def __repr__(self):
		return "Message is {}".format(self.text)