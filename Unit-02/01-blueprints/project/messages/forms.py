from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import Length, DataRequired

class MessageForm(FlaskForm):
    content = TextAreaField('Message', validators=[DataRequired(), Length(max=140)])