from project import db

class Employee(db.Model):

    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)


    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name



    def __repr__(self, first_name, last_name):
        return "{}{}".format(first_name, last_name)