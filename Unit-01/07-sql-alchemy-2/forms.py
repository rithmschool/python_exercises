from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class SignupForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=1)])
    email = StringField('E-mail', [validators.Length(min=6, max=35)])
    first_name = StringField('First-Name', [validators.Length(min=1)])
    last_name = StringField('Last-Name', [validators.Length(min=1)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
