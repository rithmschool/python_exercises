from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, SelectMultipleField, widgets
from wtforms.validators import DataRequired
from project.models import Department, Employee
from project.employees.forms import MultiCheckboxField

class NewDepartmentForm(FlaskForm):
    name = TextField('Name', validators=[DataRequired()])
    employees = MultiCheckboxField('Employees', coerce=int)

    def set_choices(self):
    	self.employees.choices = [(e.id, e.name) for e in Employee.query.all()]