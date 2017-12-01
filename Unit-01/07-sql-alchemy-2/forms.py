from flask_wtf import FlaskForm
from wtforms import StringField, validators

class UserForm(FlaskForm):
	first_name = StringField("First name:",[validators.DataRequired()])
	last_name = StringField("Last name:", [validators.DataRequired()])

class MessageForm(FlaskForm):
	text = StringField("Text:",[validators.DataRequired()])
	img = StringField("Image URL:")

class DeleteForm(FlaskForm):
	pass