from flask_wtf import FlaskForm
from wtforms import StringField, validators,PasswordField

class UserForm(FlaskForm):
	first_name = StringField('First Name', [validators.DataRequired()])
	last_name = StringField('Last Name',[validators.DataRequired()])
	username = StringField('username', [validators.DataRequired()])
	password = PasswordField('Password',[validators.DataRequired()])

class LoginForm(FlaskForm):
	username = StringField('username', [validators.DataRequired()])
	password = PasswordField('Password',[validators.DataRequired()])


class DeleteForm(FlaskForm):
	pass