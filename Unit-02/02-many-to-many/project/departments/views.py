from flask import redirect, render_template, request, url_for, Blueprint, abort, flash
from project.departments.forms import NewDepartmentForm
from project.models import Department
from flask_wtf.csrf import validate_csrf, ValidationError
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

@departments_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):
    department = Department.query.get_or_404(id)
    if request.method == b'PATCH':
        # create a new (wtf) form from the submitted form and update the name of the department
        form = NewDepartmentForm(request.form)
        department.name = form.name.data

        db.session.add(department)
        db.session.commit()
        flash("Department Updated!")
        return redirect(url_for('departments.show', id=id))

    if request.method == b'DELETE':
        # validate the csrf token or handle the error properly
        try:
            validate_csrf(request.form.get('csrf_token')) # the name of the hidden csrf token passed
        except ValidationError:
            return redirect(url_for('departments.show', id=id)) # redirect them back to show if the csrf was bad

        db.session.delete(department)
        db.session.commit()
        flash("Department Deleted!")
        return redirect(url_for('departments.index'))
    return render_template('departments/show.html', department=department)

@departments_blueprint.route('/new')
def new():
    form = NewDepartmentForm()
    return render_template('departments/new.html', form=form)

@departments_blueprint.route('/<int:id>/edit')
def edit(id):
    department = Department.query.get_or_404(id)
    if department is None:
        abort(404)

    form = NewDepartmentForm(obj=department)
    return render_template('/departments/edit.html', id=id, form=form)