from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, IntegerField, validators



class AddMessageForm(FlaskForm):
    message = StringField('Message', [validators.Length(min=1)])


class EditMessageForm(FlaskForm):
    message = StringField('Message', [validators.Length(min=1)])