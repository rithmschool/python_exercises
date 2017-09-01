from flask_wtf import FlaskForm
from wtforms import StringField, validators

class UserForm(FlaskForm):
    user_name = StringField('User Name', [validators.Length(min=1)])
    first_name = StringField('First Name', [validators.Length(min=1)])
    last_name = StringField('Last Name', [validators.Length(min=1)])
    email = StringField('E-mail', [validators.Length(min=6, max=35)])


class DeleteForm(FlaskForm):
    pass