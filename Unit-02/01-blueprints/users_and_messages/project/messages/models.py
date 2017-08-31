from project import db

# Class(es) ------------------------------------------------
class Message(db.Model):

	__tablename__ = "messages"

	# Create the columns for our users table
	id = db.Column(db.Integer, primary_key=True)
	# Using varchar on message column to limit entries to 100 characters
	message = db.Column(db.String(100))
	# Adding this column to create a relationship with the users table
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __init__(self, message, user_id):
		self.message = message
		self.user_id = user_id



