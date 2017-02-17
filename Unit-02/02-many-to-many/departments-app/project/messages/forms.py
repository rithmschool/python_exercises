from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, IntegerField, validators
from wtforms.validators import DataRequired



class AddMessageForm(FlaskForm):
    message = StringField('Message', [validators.Length(min=1)])





