from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class UserForm(FlaskForm):
	first_name = StringField("First name:",[validators.DataRequired()])
	last_name = StringField("Last name:", [validators.DataRequired()])
	username = StringField("Username:", [validators.DataRequired()])
	password = PasswordField("Password:", [validators.DataRequired()])


class MessageForm(FlaskForm):
	text = StringField("Text:",[validators.DataRequired()])
	img = StringField("Image URL:")

class DeleteForm(FlaskForm):
	pass

class LoginForm(FlaskForm):
	username = StringField("Username:", [validators.DataRequired()])
	password = PasswordField("Password:", [validators.DataRequired()])