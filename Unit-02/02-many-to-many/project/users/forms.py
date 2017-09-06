from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
	username = StringField('Username', [validators.Length(min=1)])
	password = PasswordField('password', validators=[DataRequired()])
	first_name = StringField('First Name', [validators.Length(min=1)])
	last_name = StringField('Last Name', [validators.Length(min=1)])
	email = StringField('Email', [validators.Length(min=1)])

class EditUserForm(FlaskForm):
	username = StringField('Username', [validators.Length(min=1)])
	first_name = StringField('First Name', [validators.Length(min=1)])
	last_name = StringField('Last Name', [validators.Length(min=1)])
	email = StringField('Email', [validators.Length(min=1)])

class UserLoginForm(FlaskForm):
  username = StringField('username', validators=[DataRequired()])
  password = PasswordField('password', validators=[DataRequired()])

class DeleteUserForm(FlaskForm):
	pass