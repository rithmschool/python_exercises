from flask import Blueprint, url_for, redirect, render_template, request, flash
from project import db
from project.models import Employee, Department
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
		form.set_choices()
		if form.validate():
			employee = Employee(form.name.data)
			#for d in form.departments.data:
				#employee.departments.append(Department.query.get(d))
			#employee.departments.extend([Department.query.get(department) for department in form.departments.data])
			employee.departments = [Department.query.get(department) for department in form.departments.data]
			db.session.add(employee)
			db.session.commit()
			flash('Employee created')
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
		form.set_choices()
		if form.validate():
			employee.name = form.name.data
			employee.departments = []
			#for d in form.departments.data:
				#employee.departments.append(Department.query.get(d))
			employee.departments = [Department.query.get(deptId) for deptId in form.departments.data]
			db.session.add(employee)
			db.session.commit()
			flash('Employee updated')
			return redirect(url_for('employees.show', id=employee.id))
		return render_template('employees/edit.html', department=departments)
	if request.method == b"DELETE":
		delete_form = DeleteForm(request.form)
		if delete_form.validate():
			db.session.delete(employee)
			db.session.commit()
			flash('Employee deleted')
		return redirect(url_for('employees.index'))
	delete_form = DeleteForm()
	return render_template('employees/show.html', employee=employee, delete_form=delete_form)

#GET
@employees_blueprint.route("/<int:id>/edit")
def edit(id):
	employee = Employee.query.get(id)
	departments = [department.id for department in employee.departments]
	form = EmployeeForm(name=employee.name, departments=departments)
	form.set_choices()
	return render_template('employees/edit.html', employee=employee, form=form)
