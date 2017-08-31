from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, SelectMultipleField, widgets
from wtforms.validators import DataRequired
from project.models import Department

# inheriting from a select field
class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class NewEmployeeForm(FlaskForm):
    name = TextField('Name', validators=[DataRequired()])
    years_at_company = IntegerField('Years At Company',
                                    validators=[DataRequired()])
    # holds department choices
    departments = MultiCheckboxField('Departments',
                                     coerce=int)
    # set all the choices for the departments
    def set_choices(self):
        self.departments.choices =  [(d.id, d.name) for d in Department.query.all()]
