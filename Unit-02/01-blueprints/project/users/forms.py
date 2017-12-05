from flask_wtf import FlaskForm
from wtforms import StringField, validators

class UserForm(FlaskForm):
	username = StringField('Username', [validators.DataRequired()])
	first_name = StringField('First Name', [validators.DataRequired()])
	last_name = StringField('Last Name', [validators.DataRequired()])

class DeleteForm(FlaskForm):
	pass	