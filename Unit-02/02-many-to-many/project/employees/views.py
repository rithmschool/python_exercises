from flask import Blueprint, render_template, redirect, url_for, request
from project.employees.forms import NewEmployeeForm, DeleteForm
from project.models import Employee, Department
from project import db

employees_blueprint = Blueprint(
    'employees',
    __name__,
    template_folder="templates"
    )


@employees_blueprint.route('/', methods=["POST", "GET"])
def index():
    delete_form = DeleteForm()
    if request.method == 'POST':
        form = NewEmployeeForm(request.form)
        form.set_choices()
        if form.validate_on_submit():
            new_employee = Employee(form.name.data, form.years_at_company.data)
            for department in form.departments.data:
                new_employee.departments.append(Department.query.get(department))
            db.session.add(new_employee)
            db.session.commit()
        else:
            return render_template('employees/new.html', form=form)
    return render_template('employees/index.html', employees=Employee.query.all(), delete_form = delete_form)


@employees_blueprint.route('/new', methods=["GET"])
def new():
    form = NewEmployeeForm()
    form.set_choices()
    return render_template('employees/new.html', form=form)


@employees_blueprint.route('/<int:id>/edit', methods=["GET"])
def edit(id):
    delete_form = DeleteForm()
    employee = Employee.query.get(id)
    departments = [department.id for department in employee.departments]
    form = NewEmployeeForm(departments=departments)
    form.set_choices()
    return render_template('employees/edit.html', employee=employee, form=form, delete_form = delete_form)


@employees_blueprint.route('/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
    found_employee=Employee.query.get(id)
    if request.method == b"DELETE":
        delete_form = DeleteForm(request.form)
        if delete_form.validate():
            db.session.delete(found_employee)
            db.session.commit()
        return redirect(url_for('employees.index'))
    if request.method == b"PATCH":
        form = NewEmployeeForm(request.form)
        form.set_choices()
        if form.validate():
            found_employee.name = form.name.data
            found_employee.years_at_company = form.years_at_company.data
            found_employee.departments = []
            for department in form.departments.data:
                found_employee.departments.append(Department.query.get(department))
            db.session.add(found_employee)
            db.session.commit()
            return redirect(url_for('employees.index'))
        else:
            return render_template('employees/edit.html', employee=found_employee, form=form)
    return render_template('employees/show.html', employee=found_employee)
