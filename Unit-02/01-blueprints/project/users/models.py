from project import db

class User(db.Model):
  __tablename__ = "users"

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.Text)
  email = db.Column(db.Text)
  firstname = db.Column(db.Text)
  lastname = db.Column(db.Text)
  img_url = db.Column(db.Text)
  messages = db.relationship('Message', backref='user', lazy='dynamic')

  def __init__(self, username, email, firstname, lastname, img_url):
    self.username = username
    self.email = email
    self.firstname = firstname
    self.lastname = lastname
    self.img_url = img_url

  def __repr__(self):
    return "Username {} - email {} - Name {} {} - email {} - image URL {}".format(self.username, self.email, self.firstname, self.lastname, self.image_url)