from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CreateForm(FlaskForm):
    username = StringField('username', [validators.length(min=8)])
    first_name = StringField('first_name', [validators.DataRequired()])
    last_name = StringField('last_name', [validators.DataRequired()])
    email = StringField('email', [validators.Email()])

class EditForm(FlaskForm):
    username = StringField('username', [validators.length(min=8)])
    first_name = StringField('first_name', [validators.DataRequired()])
    last_name = StringField('last_name', [validators.DataRequired()])
    email = StringField('email', [validators.Email()])
