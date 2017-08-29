from flask_wtf import FlaskForm
from wtforms import StringField, validators

class MessageForm(FlaskForm):
    message = StringField('Message', [validators.Length(min=1, max=100)])