from flask_wtf import FlaskForm
from wtforms import TextField, widgets, SelectMultipleField
from wtforms.validators import DataRequired
from project.messages.models import Message
from flask_login import current_user

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class NewTagForm(FlaskForm):
    name = TextField('Name', validators=[DataRequired()])
    messages = MultiCheckboxField('Messages',
                                     coerce=int)

    def set_choices(self):
        self.messages.choices = [(m.id, m.text) for m in current_user.messages]
    	# self.messages.choices = [(m.id, m.text) for m in Message.query.all()]

class EditTagForm(FlaskForm):
    name = TextField('Name', validators=[DataRequired()])
    messages = MultiCheckboxField('Messages',
                                     coerce=int)

    def set_choices(self):
        self.messages.choices = [(m.id, m.text) for m in current_user.messages]
    	# self.messages.choices = [(m.id, m.text) for m in Message.query.all()]