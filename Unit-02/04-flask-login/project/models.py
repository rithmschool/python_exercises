from project import db,bcrypt
from flask_login import UserMixin


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



class User(db.Model, UserMixin):
  __tablename__ = "users"

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.Text, unique=True)
  password = db.Column(db.Text)
  email = db.Column(db.Text)
  firstname = db.Column(db.Text)
  lastname = db.Column(db.Text)
  img_url = db.Column(db.Text)
  messages = db.relationship('Message', backref='user', lazy='dynamic', cascade='delete')

  def __init__(self,username, password, email, firstname, lastname, img_url):
    self.username = username
    self.password = bcrypt.generate_password_hash(password).decode('UTF-8')
    self.email = email
    self.firstname = firstname
    self.lastname = lastname
    self.img_url = img_url

  @classmethod
  def authenticate(cls, username, password):
    found_user = cls.query.filter_by(username = username).first()
    if found_user:
        authenticated_user = bcrypt.check_password_hash(found_user.password, password)
        if authenticated_user:
            return found_user
    return False

    def __repr__(self):
      return "Username {} Password hidden".format(self.username)



class Message(db.Model):
  __tablename__ = "messages"

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  message = db.Column(db.Text)
  tags = db.relationship('Tag',
                              secondary=MessageTag,
                              backref=db.backref('messages'))

  def __init__(self, message, user_id):
    self.message = message
    self.user_id = user_id


  def __repr__(self):
    return "The message is ' {} '' and user id is {}".format(self.message, self.user_id)


class Tag(db.Model):
  __tablename__ = "tags"

  id = db.Column(db.Integer, primary_key=True)
  tag = db.Column(db.Text)

  def __init__(self, tag):
    self.tag = tag

  def __repr__(self):
    return "The tag is ' {} '' and message id is {}".format(self.tag, self.message_id)