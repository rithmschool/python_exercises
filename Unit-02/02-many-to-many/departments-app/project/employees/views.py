from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
from project.employees.forms import addEmployee
from project.employees.models import Employee
from project import db


employees_blueprint = Blueprint(
    'employees',
    __name__,
    template_folder = "templates"
)

@employees_blueprint.route('/', methods=['GET', 'POST'])
def index():
    form = addEmployee(request.form)
    employees = Employee.query.all()
    if request.method == "POST" and form.validate():
        flash("you have successfully added an employee!")
        db.session.add(Employee(request.form['first_name'], request.form['last_name']))
        db.session.commit()
        return redirect(url_for('employees.index'))
    return render_template('employees/index.html', employees=employees)

@employees_blueprint.route('/new', methods=['GET', 'POST'])
def new():
    form = addEmployee(request.form)
    return render_template('employees/new.html', form=form)