from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, IntegerField, validators

class UserForm(FlaskForm):
    user_name = StringField('User Name', [validators.Length(min=1)])
    first_name = StringField('First Name', [validators.Length(min=1)])
    last_name = StringField('Last Name', [validators.Length(min=1)])
    email = StringField('E-mail', [validators.Length(min=6, max=35)])


class MessageForm(FlaskForm):
    message = StringField('Message', [validators.Length(min=1, max=100)])
