from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CreateForm(FlaskForm):
    text = StringField('Text', [validators.length(min=5)])

class EditForm(FlaskForm):
    text = StringField('Text', [validators.length(min=5)])