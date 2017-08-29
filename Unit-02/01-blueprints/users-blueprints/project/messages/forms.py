from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, IntegerField, TextAreaField, validators

class AddMessageForm(FlaskForm):
	text = TextAreaField('Text', [validators.Length(max=100)])