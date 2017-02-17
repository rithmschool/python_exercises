from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint, session
from project.messages.forms import AddMessageForm, AddFavoriteForm
from project.models import Employee, Message
from project import db, bcrypt, login_manager
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, logout_user,login_required, current_user


messages_blueprint = Blueprint(
    'messages',
    __name__,
    template_folder = "templates"
)


@login_manager.user_loader
def load_user(employee_id):
    return Employee.query.get(int(employee_id))

@messages_blueprint.route('/', methods=['GET', 'POST'])
def show(employee_id):
    this_employee = Employee.query.get(int(employee_id))
    add_favorite_form = AddFavoriteForm(request.form)
    return render_template('/messages/show.html', employee=this_employee ,messages=Message.query.all(), form= add_favorite_form)

@messages_blueprint.route('/new', methods=['GET', 'POST'])
def new(employee_id):
    this_employee = Employee.query.get(employee_id)
    message_form = AddMessageForm(request.form)
    if request.method == 'POST' and message_form.validate():
        flash("You have successfully added a message!")
        message = Message(request.form['message'], this_employee.id)
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('messages.show', employee_id=this_employee.id))


    return render_template('/messages/new.html', form=message_form, employee=this_employee)

@messages_blueprint.route('/add_favorite/<int:message_id>', methods=['GET', 'POST'])
def favorite(employee_id, message_id):
    this_employee = Employee.query.get(employee_id)
    this_message = Message.query.get(message_id)
    print (this_employee.id)
    print(this_message.id)
    if request.method == 'POST':
        this_message.employees.append(this_employee)
        db.session.add(this_message)
        db.session.commit()

    return redirect(url_for('messages.show', employee_id=this_employee.id))

@messages_blueprint.route('/show_favorites', methods=['GET', 'POST'])
def show_favorites(employee_id):
    this_employee = Employee.query.get(employee_id)
    employee_favorites = [val.message for val in this_employee.favorites]
    print(employee_favorites)
    return render_template('messages/show_favorites.html', employee = this_employee, messages= employee_favorites)

@messages_blueprint.route('/show_all', methods=['GET', 'POST'])
def show_all(employee_id):
    this_employee = Employee.query.get(employee_id)
    return render_template('messages/show_all.html', employee = this_employee, messages=this_employee.messages.all())



