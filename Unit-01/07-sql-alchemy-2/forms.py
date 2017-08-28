from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, IntegerField, validators

class UserForm(FlaskForm):
	username = StringField('Username', [validators.Length(min=1)])
	email = StringField('Email', [validators.Length(min=6, max=35)])
	first_name = StringField('First Name', [validators.Length(min=1)])
	last_name = StringField('Last Name', [validators.Length(min=1)])

class MessageForm(FlaskForm):
	text = StringField('Message', [validators.Length(min=1, max=100)])