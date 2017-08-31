from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, IntegerField, validators
# from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
	message = StringField('Message', [validators.Length(max=100)])



