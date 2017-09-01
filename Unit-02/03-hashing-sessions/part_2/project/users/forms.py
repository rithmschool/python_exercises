from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class CreateForm(FlaskForm):
    username = StringField('username', [validators.length(min=8)])
    password = PasswordField('Password', [validators.length(min=8), validators.EqualTo('confirm', message='Passwords have to match, yo?')])
    confirm = PasswordField('Confirm Password')
    first_name = StringField('first_name', [validators.DataRequired()])
    last_name = StringField('last_name', [validators.DataRequired()])
    email = StringField('email', [validators.Email()])

class EditForm(FlaskForm):
    username = StringField('username', [validators.length(min=8)])
    first_name = StringField('first_name', [validators.DataRequired()])
    last_name = StringField('last_name', [validators.DataRequired()])
    email = StringField('email', [validators.Email()])

class LoginForm(FlaskForm):
    username = StringField('username', [validators.DataRequired()], render_kw = {'placeholder': 'Username'})
    password = PasswordField('password', [validators.DataRequired()], render_kw = {'placeholder': 'Password'})