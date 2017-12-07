from project import db, bcrypt


class User(db.Model):

	__tablename__ = 'users'
	__table_args__ = {'extend_existing': True} 


	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)
	username = db.Column(db.Text, unique=True)
	password = db.Column(db.Text)
	messages = db.relationship('Message', backref='user', lazy='dynamic', cascade='all,delete')

	def __init__(self, first_name, last_name, username, password):
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.password = bcrypt.generate_password_hash(password).decode('UTF-8')


		  # notice we are making a class method here since we will be invoking this using User.authenticate()    
	@classmethod
    # let's pass some username and some password 
	def authenticate(cls, username, password):
	    found_user = cls.query.filter_by(username = username).first()
	    if found_user:
	        authenticated_user = bcrypt.check_password_hash(found_user.password, password)
	        if authenticated_user:
	            return found_user # make sure to return the user so we can log them in by storing information in the session
	    return False

class Message(db.Model):

	__tablename__ = 'messages'
	__table_args__ = {'extend_existing': True} 

# DDL
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.Text)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
# DML
	def __init__(self, content, user_id):
		self.content = content
		self.user_id = user_id	
		
