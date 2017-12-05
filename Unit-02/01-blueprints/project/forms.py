from flask_wtf import FlaskForm
from wtforms import StringField, validators

class UserForm(FlaskForm):
	first_name = StringField("First name:",[validators.DataRequired()])
	last_name = StringField("Last name:", [validators.DataRequired()])
	departments = SelectMultipleField(
		"Departments:", coerce=int, widget=widgets.ListWidget(), option_widget=widgets.CheckboxInput())

	def set_choices(self):
		self.departments.choices = [(department.id, departments.name) for department in Department.query.all()]

class DepartmentsForm(FlaskForm):
	text = StringField("Text:",[validators.DataRequired()])
	img = StringField("Image URL:")
	employees = SelectMultipleField(
		"Employees:", coerce=int, widget=widgets.ListWidget(), option_widget=widgets.CheckboxInput())

	def set_choices(self):
		self.employees.choices = [(employee.id, employee.name) for employee in Employee.query.all()]

class DeleteForm(FlaskForm):
	pass