from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class UserForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    email = StringField('E-mail', [validators.DataRequired(), validators.Email()])
    first_name = StringField('First Name', [validators.DataRequired()])
    last_name = StringField('Last Name', [validators.DataRequired()])

class MessageForm(FlaskForm):
    content = TextAreaField('Message', [validators.DataRequired()])
