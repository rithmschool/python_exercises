from flask_wtf import FlaskForm
from wtforms import StringField, validators, widgets, SelectMultipleField
from project.tags.models import Tag

class MessageForm(FlaskForm):
	text = StringField('Text', [validators.Length(min=1, max=100)])

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class EditMessageForm(FlaskForm):
	text = StringField('Text', [validators.Length(min=1, max=100)])
	tags = MultiCheckboxField('Tags',
                                coerce=int)

	def set_choices(self):
		self.tags.choices = [(t.id, t.name) for t in Tag.query.all()]

class DeleteMessageForm(FlaskForm):
	pass