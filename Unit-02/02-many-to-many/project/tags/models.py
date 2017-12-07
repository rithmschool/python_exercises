from project import db

class Tag(db.Model):
	__tablename__ = 'tags'

	id = db.Column(db.Integer, primary_key=True)
	category = db.Column(db.Text)

	def __init__(self, category):
		self.category = category