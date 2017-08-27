from flask_wtf import FlaskForm
from wtforms import StringField, validators

class UserForm(FlaskForm):
    firstname = StringField('First Name', [validators.Length(min=1)])
    lastname = StringField('Last Name', [validators.Length(min=1)])
    email = StringField('E-mail', [validators.Length(min=6, max=35)])
    img_url = StringField('Image URL', [validators.URL(require_tld=True, message='Invalid URL or incomplete URL.')])
