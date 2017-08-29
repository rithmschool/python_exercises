from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired

class MessageForm(FlaskForm):
    content = TextAreaField('Message', validators=[DataRequired()])