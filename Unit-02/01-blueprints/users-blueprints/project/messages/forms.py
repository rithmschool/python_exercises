from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, IntegerField, TextAreaField, validators
from project.users.forms import DeleteForm

class MessageForm(FlaskForm):
	text = TextAreaField('Text', [validators.Length(max=100)])