from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class UserForm(FlaskForm):
	first_name=StringField('First Name', [validators.DataRequired()],render_kw={"class":"col-4 text-center"})
	last_name=StringField('Last Name', [validators.DataRequired()],render_kw={"class":"col-4 text-center"})
	username=StringField('Username', [validators.DataRequired()],render_kw={"class":"col-4 text-center"})
	password=PasswordField('Password', [validators.DataRequired()],render_kw={"class":"col-4 text-center"})

class LoginForm(FlaskForm):
	username=StringField('Username', [validators.DataRequired()],render_kw={"class":"col-4 text-center"})
	password=PasswordField('Password', [validators.DataRequired()],render_kw={"class":"col-4 text-center"})	

	
class DeleteForm(FlaskForm):
	pass