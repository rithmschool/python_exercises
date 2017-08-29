from flask_wtf import FlaskForm
from wtforms import StringField, validators

class MessageForm(FlaskForm):
	text = StringField('Text', [validators.Length(min=1, max=100)])

class EditMessageForm(FlaskForm):
	text = StringField('Text', [validators.Length(min=1, max=100)])

class DeleteMessageForm(FlaskForm):
	pass