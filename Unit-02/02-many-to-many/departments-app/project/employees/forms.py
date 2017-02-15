from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, IntegerField, validators

class addEmployee(FlaskForm):
    first_name = StringField('First Name', [validators.Length(min=1)])
    last_name = StringField('Last Name', [validators.Length(min=1)])