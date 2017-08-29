from project import db

class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    histories = db.relationship('History', backref="owners", lazy="dynamic")

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

