from project import db


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



class User(db.Model):
  __tablename__ = "users"

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.Text)
  email = db.Column(db.Text)
  firstname = db.Column(db.Text)
  lastname = db.Column(db.Text)
  img_url = db.Column(db.Text)
  messages = db.relationship('Message', backref='user', lazy='dynamic', cascade='delete')

  def __init__(self, username, email, firstname, lastname, img_url):
    self.username = username
    self.email = email
    self.firstname = firstname
    self.lastname = lastname
    self.img_url = img_url

  def __repr__(self):
    return "Username {} - email {} - Name {} {} - email {} - image URL {}".format(self.username, self.email, self.firstname, self.lastname, self.image_url)



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