from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, widgets, validators
from project.messages.models import Message

class TagForm(FlaskForm):
	category = StringField('Category', [validators.DataRequired()])

	messages = SelectMultipleField(
        'Messages', 
        coerce=int, 
        widget=widgets.ListWidget(prefix_label=False),
        option_widget=widgets.CheckboxInput())
    
	def set_choices(self):
		self.messages.choices = [(m.id, m.content) for m in Message.query.all()]

class DeleteForm(FlaskForm):
  pass