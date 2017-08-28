from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class AuthorForm(FlaskForm):
	first_name = StringField('First Name', [validators.Length(min=1)])
	last_name = StringField('Last Name', [validators.Length(min=1)])


class BookForm(FlaskForm):
	title = StringField('Title', [validators.Length(min=1)])
	pages = IntegerField('Pages')
	publisher_name = StringField('Publisher Name', [validators.Length(min=1)])

class Edit_AuthorForm(FlaskForm):
	first_name = StringField('First Name', [validators.Length(min=1)])
	last_name = StringField('Last Name', [validators.Length(min=1)])

class Edit_BookForm(FlaskForm):
	title = StringField('Title', [validators.Length(min=1)])
	pages = IntegerField('Pages')
	publisher_name = StringField('Publisher Name', [validators.Length(min=1)])