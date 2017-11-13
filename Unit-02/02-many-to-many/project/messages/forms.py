from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectMultipleField, widgets
from project.models import Tag

class MultiCheckField(SelectMultipleField):
	widget = widgets.ListWidget(prefix_label=False)
	option_widget = widgets.CheckboxInput()

class MessageForm(FlaskForm):
	text = StringField('Message', [validators.Length(min=1, max=100)])
	tags = MultiCheckField('Tags', coerce=int)

	def set_choices(self):
		self.tags.choices=[(t.id, t.text) for t in Tag.query.all()]

class DeleteForm(FlaskForm):
	pass