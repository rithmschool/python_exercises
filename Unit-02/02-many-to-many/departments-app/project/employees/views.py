from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint, session
from project.employees.forms import addEmployee, loginEmployee, AddFavoriteForm
from project.models import Employee, Message
from project import db, bcrypt, login_manager
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, logout_user,login_required, current_user



employees_blueprint = Blueprint(
    'employees',
    __name__,
    template_folder = "templates"
)

@login_manager.user_loader
def load_user(employee_id):
    return Employee.query.get(int(employee_id))

@employees_blueprint.route('/', methods=['GET', 'POST'])
def index():
    employees = Employee.query.all()

    return render_template('employees/index.html', employees=employees)

@employees_blueprint.route('/<int:employee_id>', methods=['GET', 'POST'])
def show(employee_id):
    this_employee = Employee.query.get(employee_id)
    add_favorite_form = AddFavoriteForm(request.form)
    return render_template('employees/show.html', employee=this_employee ,messages=Message.query.all(), form= add_favorite_form)

@employees_blueprint.route('/new', methods=['GET', 'POST'])
def new():
    form = addEmployee(request.form)
    return render_template('employees/new.html', form=form)

@employees_blueprint.route('/signup', methods = ["GET", "POST"])
def signup():
    form = addEmployee()
    if not current_user.is_authenticated:
        if request.method == "POST":
            if form.validate_on_submit():
                found_employee = Employee.query.filter_by(username=form.username.data).first()
                if not found_employee:
                    try:
                        new_employee = Employee(request.form['username'], request.form['password'], request.form['first_name'],request.form['last_name'])
                        db.session.add(new_employee)
                        db.session.commit()
                        this_employee = Employee.query.filter_by(username=form.username.data).first()
                        login_user(this_employee)

                    except IntegrityError as e:
                        return render_template('employees/signup.html', form=form)
                    return redirect(url_for('employees.show', employee_id= this_employee.id))
                else:
                    flash("User credentials are invalid")
    else:
        flash("User is logged in already")
        return redirect(url_for('employees.index'))
    return render_template('employees/signup.html', form=form)

@employees_blueprint.route('/login', methods = ["GET", "POST"])
def login():
    form = loginEmployee()
    if not current_user.is_authenticated:
        if request.method == "POST":

            if form.validate_on_submit():

                found_employee = Employee.query.filter_by(username = form.username.data).first()
                if found_employee:
                    authenticated_user = bcrypt.check_password_hash(found_employee.password, request.form['password'])
                    if authenticated_user:
                        login_user(found_employee)
                        print(found_employee.username)
                        flash("Welcome to the app!")
                        return redirect(url_for('employees.show', employee_id=found_employee.id))
                    else:
                        flash("Credentials not valid")
                else:
                    flash("Credentials not valid")
    else:
        flash("User is logged in already")
        return redirect(url_for('employees.index'))
    return render_template('employees/login.html', form=form)

@employees_blueprint.route('/logout', methods = ["GET", 'POST'])
@login_required
def logout():

    form = loginEmployee()
    if current_user.is_authenticated:
        logout_user()
        flash("you have been logged out")
    else:
        flash("you are not logged in")
        return redirect(url_for('employees.index'))

    return render_template('employees/index.html')

@employees_blueprint.route('/welcome')
def welcome():
    return render_template('employees/welcome.html')