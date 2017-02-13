
from app import db

class Snack(db.Model):
    __tablename__ = "snacks"

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __repr__(self):
        return "Snack: {}, Type of Snack: {}".format(self.name, self.type)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    type = db.Column(db.Integer)


    db.create_all()