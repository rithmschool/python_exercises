from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class UserForm(FlaskForm):
	username = StringField('Username', [validators.Length(min=1)])
	email = StringField('Email', [validators.Length(min=6, max=35)])
	first_name = StringField('First Name', [validators.Length(min=1)])
	last_name = StringField('Last Name', [validators.Length(min=1)])
	password = PasswordField('password', [validators.Length(min=1)])

class SignupForm(FlaskForm):
	username = StringField('Username', [validators.Length(min=1)])
	email = StringField('Email', [validators.Length(min=6, max=35)])
	first_name = StringField('First Name', [validators.Length(min=1)])
	last_name = StringField('Last Name', [validators.Length(min=1)])
	password = PasswordField('password', [validators.Length(min=1)])

class LoginForm(FlaskForm):
	username = StringField('Username', [validators.Length(min=1)])
	password = PasswordField('password', [validators.Length(min=1)])
