from flask import redirect, render_template, request, url_for, Blueprint
from project.departments.forms import NewDepartmentForm
from project.models import Department, Employee
from project import db

departments_blueprint = Blueprint(
    'departments',
    __name__,
    template_folder='templates'
)

@departments_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = NewDepartmentForm(request.form)
        form.set_choices()
        if form.validate_on_submit():
            department = Department(form.name.data)
            for employee in form.employees.data:
                department.employees.append(Employee.query.get(employee))
            db.session.add(department)
            db.session.commit()
            return redirect(url_for('departments.index'))
        else:
            return render_template('departments/new.html', form=form)
    return render_template('departments/index.html', departments=Department.query.all())

@departments_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):
    department = Department.query.get_or_404(id)
    if request.method == b'DELETE':
        db.session.delete(department)
        db.session.commit()
        return redirect(url_for('departments.index'))
    if request.method == b'PATCH':
        form = NewDepartmentForm(request.form)
        form.set_choices()
        if form.validate():
            department.name = form.name.data
            department.employees = []
            for employee in form.employees.data:
                department.employees.append(Employee.query.get(employee))
            db.session.add(department)
            db.session.commit()
            return redirect(url_for('departments.index'))
        else:
            return render_template('departments/edit.html', form=form)
    return render_template('departments/show.html', department=department)

@departments_blueprint.route('/new')
def new():
    form = NewDepartmentForm()
    form.set_choices()
    return render_template('departments/new.html', form=form)

@departments_blueprint.route('<int:id>/edit', methods=["GET"])
def edit(id):
    found_dept = Department.query.get(id)
    employees = [employee.id for employee in found_dept.employees]
    form = NewDepartmentForm(employees=employees)
    form.set_choices()
    return render_template('departments/edit.html', department=found_dept, form=form)
