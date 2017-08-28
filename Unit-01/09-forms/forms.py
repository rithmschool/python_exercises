from flask_wtf import FlaskForm
from wtforms import StringField, validators

class NewUser(FlaskForm):
    username = StringField('Username', [validators.Length(min=1)])
    email = StringField('E-Mail', [validators.Length(min=6, max=35)])
    first_name = StringField('First Name', [validators.Length(min=1)])
    last_name = StringField('Last Name', [validators.Length(min=1)])
    image_url = StringField('Image URL', [validators.Length(min=7)])

class NewMessage(FlaskForm):
    message = StringField('Message:', [validators.Length(min=1)])