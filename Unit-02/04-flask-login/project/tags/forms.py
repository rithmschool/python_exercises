from flask_wtf import FlaskForm
from wtforms import TextField, SelectMultipleField, widgets
from wtforms.validators import DataRequired
from project.models import Message

class MultiCheckField(SelectMultipleField):
	widget = widgets.ListWidget(prefix_label=False)
	option_widget = widgets.CheckboxInput()

class TagForm(FlaskForm):
	text = TextField('Text', validators = [DataRequired()])
	messages = MultiCheckField('Messages', coerce=int)

	def set_choices(self):
		self.messages.choices=[(m.id, m.text) for m in Message.query.all()]


class DeleteForm(FlaskForm):
	pass

