from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, validators,widgets
from project.tags.models import Tag

class MessageForm(FlaskForm):
	content = StringField('Content', [validators.DataRequired()])

	tags = SelectMultipleField(
  		'Tags',
  		coerce=int,
  		widget=widgets.ListWidget(prefix_label=False),
  		option_widget=widgets.CheckboxInput()
  	)

	def set_choices(self):
  		self.tags.choices = [(t.id, t.category) for t in Tag.query.all()]


class DeleteForm(FlaskForm):
  pass