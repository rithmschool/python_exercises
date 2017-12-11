from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, SelectMultipleField, widgets
from wtforms.validators import DataRequired
from project.models import Employee


class NewDepartmentForm(FlaskForm):
    name = TextField('Name', validators=[DataRequired()])

    employees = SelectMultipleField(
    	'Employees',
    	coerce=int,
    	widget=widgets.ListWidget(prefix_label=True),
    	option_widget=widgets.CheckboxInput())

    def set_choices(self):
    	self.employees.choices = [(employee.id, employee.name) for employee in Employee.query.all()]


class DeleteForm(FlaskForm):
	pass 