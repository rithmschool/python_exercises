from project import db, bcrypt
from flask_login import UserMixin

class User(db.Model, UserMixin):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    email = db.Column(db.Text, unique=True)
    messages = db.relationship('Message', cascade="all, delete-orphan", backref='user', lazy='dynamic')

    def __init__(self, user_name, password, first_name, last_name, email):
        self.user_name = user_name
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8')
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __repr__(self):
        return "User {} {}'s user name is {}".format(self.first_name, self.last_name,
                                                        self.user_name)

    # making a class method here since we will be invoking this using User.authenticate()    
    @classmethod
    # let's pass some username and some password 
    def authenticate(cls, user_name, password):
        found_user = cls.query.filter_by(user_name=user_name).first()
        if found_user:
            authenticated_user = bcrypt.check_password_hash(found_user.password, password)
            if authenticated_user:
                return found_user # return the user so we can log them in by storing information in the session
        return False


message_tag_table = db.Table('message_tags',
    db.Column('message_id', db.Integer, db.ForeignKey('messages.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
)


class Message(db.Model):

    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    tags = db.relationship('Tag', secondary=message_tag_table, backref=db.backref('messages'))

    def __init__(self, message, user_id):
        self.message = message
        self.user_id = user_id



class Tag(db.Model):

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)

    def __init__(self, text):
        self.text = text
