from flask import Blueprint, url_for, redirect, render_template, request, flash
from project import db
from project.models import Employee
from project.forms import EmployeeForm, DeleteForm

employees_blueprint = Blueprint(
	'employees',
	__name__,
	template_folder='templates/employees')

#GET, POST
@employees_blueprint.route('/', methods=["GET", "POST"])
def index():
	if request.method = "POST"
		form = EmployeeForm(request.form)
		if form.validate():
			employee = Department(form.employee_name.data)
			employee.departments = form.deparments.data
			db.session.add(employee)
			db.session.commit()
			return redirect(url_for('employees.index'))
		return render_template('new.html', form=form)
	return render_template('index.html', employees=Employee.query.all())

#GET
@employees_blueprint.route("/new")
def new():
	form = EmployeeForm()
	form.set_choices()
	return render_template('new.html', form=form)

#GET, PATCH, DELETE
@employees_blueprint.route("/show", methods=["GET", "PATCH", "DELETE"])
def show():
	#get employee
	if request.method = b"PATCH":
		pass
	if request.method = b"DELETE":
		pass
	render_template('show.html', employee=employee)

#GET
@employees_blueprint.route("/edit")
def edit():
	#get form