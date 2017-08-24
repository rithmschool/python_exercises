from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CreateUserForm(FlaskForm):
    username = StringField('Username', [validators.length(min=8)])
    first_name = StringField('FirstName', [validators.InputRequired()])
    last_name = StringField('LastName', [validators.InputRequired()])
    email = StringField('Email', [validators.Email()])

class EditUserForm(FlaskForm):
    username = StringField('Username', [validators.length(min=8)])
    first_name = StringField('FirstName', [validators.InputRequired()])
    last_name = StringField('LastName', [validators.InputRequired()])
    email = StringField('Email', [validators.Email()])

class DeleteUserForm(FlaskForm):
    pass

class CreateMessageForm(FlaskForm):
    text = StringField('Text', [validators.length(min=5)])

class EditMessageForm(FlaskForm):
    text = StringField('Text', [validators.length(min=5)])

class DeleteMessageForm(FlaskForm):
    pass
