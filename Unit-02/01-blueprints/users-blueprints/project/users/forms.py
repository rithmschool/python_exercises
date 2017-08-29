from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, IntegerField, TextAreaField, validators

class AddUserForm(FlaskForm):
	username = StringField('Username', [validators.Length(min=1)])
	email = StringField('Email', [validators.Length(min=5)])
	first_name = StringField('First Name', [validators.Length(min=1)])
	last_name = StringField('Last Name', [validators.Length(min=1)])