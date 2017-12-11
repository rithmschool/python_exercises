from project import db, bcrypt
from flask_login import UserMixin

class User(db.Model, UserMixin):

  __tablename__ = "users"

  # columns!
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.Text, unique=True)
  password = db.Column(db.Text)
  first_name = db.Column(db.Text)
  last_name = db.Column(db.Text)
  profile_link = db.Column(db.Text)
  messages = db.relationship('Message', backref="user", lazy="dynamic", cascade="all,delete")

  def __init__(self, first_name, last_name, username, password, profile_link):
    self.first_name = first_name
    self.last_name = last_name
    self.profile_link = profile_link
    self.username = username
    self.password = bcrypt.generate_password_hash(password).decode('UTF-8')

  @classmethod
  def authenticate(cls, username, password):
    found_user = cls.query.filter_by(username=username).first()
    if found_user:
      is_authenticated = bcrypt.check_password_hash(found_user.password, password)
      if is_authenticated:
        return found_user
    return False