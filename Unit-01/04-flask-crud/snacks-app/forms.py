from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, IntegerField, validators

class SignupForm(FlaskForm):
    name = StringField('name', [validators.Length(min=1)])
    image_url = StringField('image_url', [validators.Length(min=6, max=35)])

