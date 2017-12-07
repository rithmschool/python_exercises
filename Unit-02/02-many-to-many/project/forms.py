from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, validators, widgets
from project.models import Department, Employee

class DepartmentForm(FlaskForm):
	name = StringField("Department name:", [validators.DataRequired()])
	employees = SelectMultipleField(
		"Employees:", coerce=int, widget=widgets.ListWidget(prefix_label=False), option_widget=widgets.CheckboxInput())

	def set_choices(self):
		self.employees.choices = [(employee.id, employee.name) for employee in Employee.query.all()]


class EmployeeForm(FlaskForm):
	name = StringField("Employee name:", [validators.DataRequired()])
	departments = SelectMultipleField(
		"Departments:", coerce=int, widget=widgets.ListWidget(prefix_label=False), option_widget=widgets.CheckboxInput())

	def set_choices(self):
		self.departments.choices = [(department.id, department.name) for department in Department.query.all()]

class DeleteForm(FlaskForm):
	pass
