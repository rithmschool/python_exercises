from flask_wtf import FlaskForm
from wtforms import StringField, validators

class UserForm(FlaskForm):
  first_name = StringField('First Name', [validators.DataRequired()])
  last_name = StringField('Last Name', [validators.DataRequired()])
  profile_link = StringField('Profile Link', [validators.DataRequired()])


class DeleteForm(FlaskForm):
  pass