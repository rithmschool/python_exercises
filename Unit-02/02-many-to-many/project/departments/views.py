from flask import redirect, render_template, request, url_for, Blueprint
from project.departments.forms import NewDepartmentForm, DeleteForm
from project.models import Department
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
        if form.validate_on_submit():
            department = Department(form.name.data)
            db.session.add(department)
            db.session.commit()
            return redirect(url_for('departments.index'))
        else:
            return render_template('departments/new.html', form=form)
    return render_template('departments/index.html', departments=Department.query.all())

@departments_blueprint.route('/<int:id>', methods=['GET', 'DELETE', 'PATCH'])
def show(id):
    delete_form = DeleteForm()
    department = Department.query.get_or_404(id)
    if request.method == b"DELETE":
        delete_form = DeleteForm(request.form)
        if delete_form.validate():
            db.session.delete(department)
            db.session.commit()
        return redirect(url_for('departments.index'))    
    if request.method == b'PATCH':
        department_form = NewDepartmentForm(request.form)
        if department_form.validate():
            department.name = department_form.name.data
            db.session.add(department)
            db.session.commit()
            return redirect(url_for('departments.index'))
        return render_template('departments/edit.html', department=department, form=department_form)
    return render_template('departments/show.html', department=department, delete_form = delete_form)

@departments_blueprint.route('/new')
def new():
    form = NewDepartmentForm()
    return render_template('departments/new.html', form=form)


@departments_blueprint.route('/<int:id>/edit', methods=["GET"])
def edit(id):
    department = Department.query.get(id)
    department_form = NewDepartmentForm(obj=department)
    return render_template('departments/edit.html', department=department, form=department_form)


