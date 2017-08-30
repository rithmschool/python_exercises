from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, SelectMultipleField, widgets
from wtforms.validators import DataRequired
from project.models import Department


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class NewEmployeeForm(FlaskForm):
    name = TextField('Name', validators=[DataRequired()])
    years_at_company = IntegerField('Years At Company',
                                    validators=[DataRequired()])
    departments = MultiCheckboxField('Departments',
                                     coerce=int)
    def set_choices(self):
        self.departments.choices = [(d.id, d.name) for d in Department.query.all()]
