from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, validators, widgets
from project.models import Department, Employee

class DepartmentForm(FlaskForm):
	department_name = StringField("Department name:", [validators.DataRequired()])
	employees = SelectMultipleField(
		"Employees:", coerce=int, widget=widgets.ListWidget(), option_widget=widgets.CheckboxInput())

	def set_choices(self):
		self.employees.choices = [(employee.id, employee.name) for employee in Employee.query.all()]


class EmployeeForm(FlaskForm):
	employee_name = StringField("Department name:", [validators.DataRequired()])
	departments = SelectMultipleField(
		"Departments:", coerce=int, widget=widgets.ListWidget(), option_widget=widgets.CheckboxInput())

	def set_choices(self):
		self.departments.choices = [(department.id, departments.name) for department in Department.query.all()]

class DeleteForm(FlaskForm):
	pass
