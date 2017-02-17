from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, IntegerField, validators
from wtforms.validators import DataRequired

class addEmployee(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    first_name = StringField('First Name', [validators.Length(min=1)])
    last_name = StringField('Last Name', [validators.Length(min=1)])

class loginEmployee(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class AddFavoriteForm(FlaskForm):
    message = StringField('Message', [validators.Length(min=1)])



