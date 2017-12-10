from flask_wtf import FlaskForm
from wtforms import TextAreaField, SelectMultipleField, widgets, validators
from project.models import Tag

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class MessageForm(FlaskForm):
	content=TextAreaField('Content', [validators.DataRequired(), validators.length(max=280)], render_kw={"rows": 3, "class": "text-center col-6"})
	tags = MultiCheckboxField('Tags', coerce=int)

	def set_choices(self):
		self.tags.choices = [(t.id, t.text) for t in Tag.query.all()]

class DeleteForm(FlaskForm):
	pass