from project import db, bcrypt
from flask_login import UserMixin


join_table = db.Table('employee_favorites',
                      db.Column('employee_id', db.Integer, db.ForeignKey('employees.id')),
                      db.Column('message_id', db.Integer, db.ForeignKey('messages.id'))
                      )

class Employee(db.Model, UserMixin):

    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    favorites = db.relationship('Message', secondary=join_table, backref=db.backref('employees'))
    messages = db.relationship('Message', backref='employee',
                               lazy='dynamic')

    def __init__(self,username, password, first_name, last_name):
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8')
        self.first_name = first_name
        self.last_name = last_name

    # def __repr__(self, first_name, last_name):
    #     return "{}{}".format(first_name, last_name)





class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))

    def __init__(self, message, employee_id):
        self.message = message
        self.employee_id = employee_id

    # def __repr__(self, message):
    #     return '{}'.format(message)


