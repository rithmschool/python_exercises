from project import db, bcrypt # project refers to __init__.py file

#db.create_All() in terminal creates table
class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    password = db.Column(db.Text)
    messages = db.relationship(
        'Message', backref='user', lazy='dynamic', cascade='all,delete')

    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8')

    def __repr__(self):
        return "The student's name is {} {}".format(self.first_name, self.last_name)


class Message(db.Model):

  __tablename__ = "messages"

  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.Text)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id
