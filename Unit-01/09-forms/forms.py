from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, IntegerField, validators

class UserForm(FlaskForm):
    username = StringField('Username', [validators.Length(max=35)])
    email = StringField('E-mail', [validators.Length(min=6, max=35)])
    first_name = StringField('First', [validators.Length(min=1)])
    last_name = StringField('Last', [validators.Length(min=1)])
