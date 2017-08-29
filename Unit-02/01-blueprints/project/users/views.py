from flask import Blueprint, redirect, url_for, render_template, flash, request
from project.users.models import User
from project.users.forms import UserForm
from project import db

users_blueprint = Blueprint(
    'users',
    __name__,
    template_folder='templates'
)

@users_blueprint.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        form = UserForm(request.form)
        if form.validate():
            new_user = User(request.form.get('username'), request.form.get('email'), request.form.get('first_name'), request.form.get('last_name'))
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('users.index'))
        return render_template('users/new.html', form=form)
    return render_template('users/index.html', users=User.query.all())

@users_blueprint.route('/new')
def new():
    form = UserForm()
    return render_template('users/new.html', form=form)

@users_blueprint.route('/<int:id>/edit')
def edit(id):
    user=User.query.get(id)
    form = UserForm(obj=user)
    return render_template('users/edit.html', form=form, user=user)

@users_blueprint.route('/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
    found_user = User.query.get(id)
    if request.method == b"PATCH":
        form = UserForm(request.form)
        if form.validate():
            found_user.username = request.form.get('username')
            found_user.email = request.form.get('email')
            found_user.first_name = request.form.get('first_name')
            found_user.last_name = request.form.get('last_name')
            db.session.add(found_user)
            db.session.commit()
            return redirect(url_for('users.index'))
        return render_template('owners/edit.html', form=form, user=found_user)
    if request.method == "DELETE":
        db.session.add(found_user)
        db.session.commit()
        return redirect(url_for('users.index'))
    return redirect('owners/show.html', user=found_user)
