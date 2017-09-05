from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, IntegerField, TextAreaField, validators, SelectMultipleField, widgets
from project.users.forms import DeleteForm
from project.models import Tag
from project.tags.forms import MultiCheckboxField

class MessageForm(FlaskForm):
	text = TextAreaField('Text', [validators.Length(max=100)])
	tags = MultiCheckboxField('tags', coerce=int)

	def set_choices(self):
		self.tags.choices = [(t.id, t.text) for t in Tag.query.all()]