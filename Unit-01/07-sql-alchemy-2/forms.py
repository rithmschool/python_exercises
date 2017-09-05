from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError
from wtforms.validators import InputRequired, Email


# class UserForm(FlaskForm):
#     username = StringField('User Name', [validators.Length(min=3)])
#     email = StringField('E-mail', [validators.Length(min=6, max=35)])
#     firstname = StringField('First Name', [validators.Length(min=1)])
#     lastname = StringField('Last Name', [validators.Length(min=1)])
#     img_url = StringField('Image URL', [validators.URL(require_tld=False, message='Invalid URL or incomplete URL.')])


# def validate_unique(form, field):
#   if len(field.data) < 5:
#     raise ValidationError('Name must be less than 50 characters')


# class UserForm(FlaskForm):
#   username = StringField('User Name', [validators.Length(min=3), validate_unique])
#   email = StringField('E-mail', [validators.Email()])
#   firstname = StringField('First Name', [validators.Length(min=1)])
#   lastname = StringField('Last Name', [validators.Length(min=1)])
#   img_url = StringField('Image URL', [validators.URL(require_tld=False, message='Invalid URL or incomplete URL.')])

class MessageForm(FlaskForm):
  message = StringField('Message', [validators.Length(min=3)])