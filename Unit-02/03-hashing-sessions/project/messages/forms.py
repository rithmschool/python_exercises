from flask_wtf import FlaskForm
from wtforms import StringField, validators 

class MessageForm(FlaskForm):
	text = StringField('Message', [validators.DataRequired()])

class DeleteForm(FlaskForm):
	pass	