from flask_wtf import FlaskForm

from wtforms import StringField,validators

class NewUserForm(FlaskForm):
	username= StringField('Username:',[validators.Length(min=1)])
	email= StringField('Email:',[validators.Length(min=1)])
	first_name= StringField('First name:',[validators.Length(min=1)])
	last_name= StringField('Last name:',[validators.Length(min=1)])

class NewMessageForm(FlaskForm):
	title= StringField('Message:', [validators.Length(min=1)])

##no validation because delete the form is empty
class EditUserForm(FlaskForm):
	name= StringField('User information:',)

class EditMessageForm(FlaskForm):
	title= StringField('Message:',)
