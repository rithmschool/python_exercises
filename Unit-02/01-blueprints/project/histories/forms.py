from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class HistoryForm(FlaskForm):
    city_lived_in = StringField('city_lived_in', validators=[DataRequired()])