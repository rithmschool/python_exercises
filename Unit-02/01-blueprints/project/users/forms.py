from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Email

class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First Name', validators = [DataRequired(), Length(min=1)])
    last_name = StringField('Last Name', validators = [DataRequired(), Length(min=1)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])