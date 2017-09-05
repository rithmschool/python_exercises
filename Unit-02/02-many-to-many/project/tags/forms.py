from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, widgets, StringField, validators
from project.models import Message


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class TagForm(FlaskForm):
  tag = StringField('Tag', [validators.Length(min=3)])

  messages = MultiCheckboxField('Messages', coerce=int)

  def set_choices(self):
        self.messages.choices =  [(d.id, d.message) for d in Message.query.all()]