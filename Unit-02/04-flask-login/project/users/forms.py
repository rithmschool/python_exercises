from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
  username = StringField('User Name', [validators.Length(min=3)])
  password = PasswordField('Password', validators=[DataRequired()])
  email = StringField('E-mail', [validators.Email()])
  firstname = StringField('First Name', [validators.Length(min=1)])
  lastname = StringField('Last Name', [validators.Length(min=1)])
  img_url = StringField('Image URL', [validators.URL(require_tld=False, message='Invalid or incomplete URL.')])

class UserLogin(FlaskForm):
  username = StringField('User Name', [validators.Length(min=3)])
  password = PasswordField('Password', validators=[DataRequired()])