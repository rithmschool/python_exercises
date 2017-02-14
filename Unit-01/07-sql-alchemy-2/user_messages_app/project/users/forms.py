from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, IntegerField, validators


class AddUserForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=1)])
    email = StringField('Email', [validators.Email(message = "Must be a valid email")])
    first_name = StringField('First Name', [validators.Length(min=1)])
    last_name = StringField('Last Name', [validators.Length(min=1)])

class EditUserForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=1)])
    email = StringField('Email', [validators.Email(message = "Must be a valid email")])
    first_name = StringField('First Name', [validators.Length(min=1)])
    last_name = StringField('Last Name', [validators.Length(min=1)])

class DeleteUserForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=1)])

