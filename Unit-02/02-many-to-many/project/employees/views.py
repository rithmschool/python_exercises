from flask import Blueprint, url_for, redirect, render_template, request, flash
from project import db
from project.models import Employee
from project.forms import EmployeeForm, DeleteForm

employees_blueprint = Blueprint(
	'employees',
	__name__,
	template_folder='templates')

#GET, POST
@employees_blueprint.route('/', methods=["GET", "POST"])
def index():
	if request.method == "POST":
		form = EmployeeForm(request.form)
		if form.validate():
			employee = Employee(form.name.data)
			employee.departments = [Department.query.get(department) for department in form.departments.data]
			db.session.add(employee)
			db.session.commit()
			return redirect(url_for('employees.index'))
		return render_template('employees/new.html', form=form)
	return render_template('employees/index.html', employees=Employee.query.all())

#GET
@employees_blueprint.route("/new")
def new():
	form = EmployeeForm()
	form.set_choices()
	return render_template('employees/new.html', form=form)

#GET, PATCH, DELETE
@employees_blueprint.route("/<int:id>", methods=["GET", "PATCH", "DELETE"])
def show(id):
	employee = Employee.query.get(id)
	if request.method == b"PATCH":
		form = EmployeeForm(request.form)
		if form.validate():
			employee.name = form.name.data
			employee.departments = [Department.query.get(department.id) for department in form.departments.data]
			db.session.add(employee)
			db.session.commit()
			return redirect(url_for('employees.show'))
		return render_template('employees/edit.html', department=departments)
	if request.method == b"DELETE":
		form = EmployeeForm(request.form)
		if form.validate():
			db.session.delete(employee)
			db.session.commit()
		return redirect('url_for(employees.index')
	return render_template('employees/show.html', employee=employee)

#GET
@employees_blueprint.route("/<int:id>/edit")
def edit(id):
	employee = Employee.query.get(id)
	form = EmployeeForm(obj=employee)
	form.set_choices()
	return render_template('employees/edit.html', form=form)