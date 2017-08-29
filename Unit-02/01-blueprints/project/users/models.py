from project import db

class User(db.Model):

    __tablename__ = "users"

    # create the essential columns for our table
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    email = db.Column(db.Text)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    image_url = db.Column(db.Text)

    def __init__(self, username, email, first_name, last_name, image_url):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.image_url = image_url

    def __repr__(self):
        return "Username: {}, Email: {}, First: {}, Last: {}".format(self.username, self.email, self.first_name, self.last_name)