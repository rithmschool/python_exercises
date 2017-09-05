from flask_wtf import FlaskForm
from wtforms import StringField, widgets, SelectMultipleField
from wtforms.validators import DataRequired
from project.models import Message
from project.users.forms import DeleteForm

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class TagForm(FlaskForm):
	text = StringField('Text', validators=[DataRequired()])
	messages = MultiCheckboxField('messages', coerce=int)

	def set_choices(self):
		self.messages.choices = [(m.id, m.text) for m in Message.query.all()]