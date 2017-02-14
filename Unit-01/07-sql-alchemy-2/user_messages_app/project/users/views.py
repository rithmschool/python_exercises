from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
from project.users.forms import AddUserForm, EditUserForm,DeleteUserForm
from project.users.models import User
from project import db


users_blueprint = Blueprint(
    'users',
    __name__,
    template_folder = "templates"
)


@users_blueprint.route('/', methods=['GET', 'POST'])
def index():
    user_form = AddUserForm(request.form)

    if request.method == "POST" and user_form.validate():
        flash("You have successfully added a user!")
        db.session.add(User(request.form['username'], request.form['email'],request.form['first_name'],request.form['last_name']))
        db.session.commit()
        return redirect(url_for('users.index'))
    elif request.method == "POST" and not user_form.validate():
        return render_template('users/new.html', form=user_form)
    return render_template('users/index.html', users=User.query.order_by(User.id).all())

@users_blueprint.route('/<int:id>/update', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def update(id):
    edit_form = EditUserForm(request.form)

    if request.method == b"PATCH" and edit_form.validate():
        user_to_update = User.query.get(id)
        user_to_update.username = request.form['username']
        user_to_update.email = request.form['email']
        user_to_update.first_name = request.form['first_name']
        user_to_update.last_name = request.form['last_name']
        db.session.add(user_to_update)
        db.session.commit()
        return redirect(url_for('users.index'))

    if request.method == b"DELETE":
        user_to_delete = User.query.get(id)
        db.session.delete(user_to_delete)
        db.session.commit()
        return redirect(url_for('users.index'))

    elif request.method == b"PATCH" and not edit_form.validate():
        return render_template('users/edit.html', user=User.query.get(id), form=edit_form)

    return render_template('users/index.html', users=User.query.all())


@users_blueprint.route('/new', methods=['GET', 'POST'])
def newUser():
    user_form = AddUserForm(request.form)
    return render_template('users/new_user.html', form=user_form)


@users_blueprint.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    edit_form = EditUserForm(request.form)
    delete_form = DeleteUserForm(request.form)
    return render_template('users/edit.html', user=User.query.get(id),edit_form=edit_form, delete_form=delete_form)
