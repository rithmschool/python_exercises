from flask import Blueprint, url_for, redirect, render_template, request, flash
from project import db
from project.models import Department
from project.forms import DepartmentForm, DeleteForm

departments_blueprint = Blueprint(
	'departments',
	__name__,
	template_folder='templates/departments'
)

#GET, POST
@departments_blueprint.route('/', methods=["GET", "POST"])
def index():
	if request.method = "POST"
		form = DepartmentForm(request.form)
		if form.validate():
			department = Department(form.department_name.data)
			department.employees = form.employees.data
			db.session.add(department)
			db.session.commit()
			return redirect(url_for('departments.index'))
		return render_template('new.html', form=form)
	return render_template('index.html', departments=Department.query.all())

#GET
@departments_blueprint.route("/new")
def new():
	form = DepartmentForm()
	form.set_choices()
	return render_template('new.html', form=form)

#GET, PATCH, DELETE
@departments_blueprint.route("/show", methods=["GET", "PATCH", "DELETE"])
def show():
	#get department
	if request.method = b"PATCH":
		pass
	if request.method = b"DELETE":
		pass
	render_template('show.html', department=department)

#GET
@departments_blueprint.route("/edit")
def edit():
	#get form
	render_template('edit.html', form=form)