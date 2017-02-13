from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, IntegerField, validators

class NewForm(FlaskForm):
	name = StringField('Name', [validators.DataRequired()])
	type = StringField('Type', [validators.Length(min=1)])
	rating = IntegerField('Rating', [validators.DataRequired()])

