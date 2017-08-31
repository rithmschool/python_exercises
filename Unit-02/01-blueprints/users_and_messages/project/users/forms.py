from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, IntegerField, validators
# from wtforms.validators import DataRequired

class UserForm(FlaskForm):
	username = StringField('Username', [validators.Length(min=5)])
	email = StringField('E-mail', [validators.Length(min=6, max=35)])
	first_name = StringField('Fist Name', [validators.Length(min=2)])
	last_name = StringField('Fist Name', [validators.Length(min=2)])
# 	# password = PasswordField('Password', [
# 	# 	validators.DataRequired(),
# 	# 	validators.EqualTo('confirm', message='Passwords must match')
# 	# ])

