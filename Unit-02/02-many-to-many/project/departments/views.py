from flask import Blueprint, url_for, redirect, render_template, request, flash
from project import db
from project.models import Department
from project.forms import DepartmentForm, DeleteForm

departments_blueprint = Blueprint(
	'departments',
	__name__,
	template_folder='templates')

#GET, POST
@departments_blueprint.route('/', methods=["GET", "POST"])
def index():
	if request.method == "POST":
		form = DepartmentForm(request.form)
		if form.validate():
			department = Department(form.name.data)
			department.employees = [Employee.query.get(employee) for employee in form.employees.data]
			db.session.add(department)
			db.session.commit()
			return redirect(url_for('departments.index'))
		return render_template('departments/new.html', form=form)
	return render_template('departments/index.html', departments=Department.query.all())

#GET
@departments_blueprint.route("/new")
def new():
	form = DepartmentForm()
	form.set_choices()
	return render_template('departments/new.html', form=form)

#GET, PATCH, DELETE
@departments_blueprint.route("/<int:id>", methods=["GET", "PATCH", "DELETE"])
def show(id):
	department = Department.query.get(id)
	if request.method == b"PATCH":
		form = DepartmentForm(request.form)
		if form.validate():
			department.name = form.name.data
			department.employees = [Employee.query.get(employee) for employee in form.employees.data]
			db.session.add(department)
			db.session.commit()
			return redirect(url_for('departments.show', id=department.id))
		return render_template('departments/edit.html', department=departments)
	if request.method == b"DELETE":
		delete_form = DeleteForm(request.form)
		if delete_form.validate():
			db.session.delete(department)
			db.session.commit()
		return redirect(url_for('departments.index'))
	delete_form = DeleteForm()
	return render_template('departments/show.html', department=department, delete_form=delete_form)

#GET
@departments_blueprint.route("/<int:id>/edit")
def edit(id):
	department = Department.query.get(id)
	form = DepartmentForm(obj=department)
	form.set_choices()
	return render_template('departments/edit.html', department=department, form=form)