from flask import redirect, request, render_template, Blueprint, url_for, flash
from project.models import User
from project.users.forms import UserForm, DeleteForm
from sqlalchemy.exc import IntegrityError
from project import db

# let's create the users_blueprint to register in our __init__.py
users_blueprint = Blueprint(
    'users',
    __name__,
    template_folder='templates'
)


@users_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = UserForm(request.form)
        if form.validate():
            user_name = request.form.get('user_name')
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            email = request.form.get('email')

            db.session.add(User(user_name, first_name, last_name, email))

            try:
                db.session.commit()
                flash('User created!')
            except IntegrityError as err:
                print(err)
                return render_template('users/new.html', form=form)

            return redirect(url_for('users.index'))
        else:
            return render_template('users/new.html', form=form)
    return render_template('users/index.html', users=User.query.order_by(User.user_name).all())


@users_blueprint.route('/new')
def new():
    form = UserForm()
    return render_template('users/new.html', form=form)


@users_blueprint.route('/<int:id>/edit')
def edit(id):
    found_user = User.query.get_or_404(id)
    form = UserForm(obj=found_user)
    return render_template('users/edit.html', form=form, user=found_user)


@users_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):
    found_user = User.query.get_or_404(id)
    if request.method == b'PATCH':
        form = UserForm(request.form)
        if form.validate():
            found_user.user_name = request.form.get('user_name')
            found_user.first_name = request.form.get('first_name')
            found_user.last_name = request.form.get('last_name')
            found_user.email = request.form.get('email')

            db.session.add(found_user)
            db.session.commit()
            return redirect(url_for('users.index'))
        else:
            return render_template('users/edit.html', form=form, user=found_user)
    if request.method == b'DELETE':
        form = DeleteForm(request.form)
        if form.validate():
            db.session.delete(found_user)
            db.session.commit()
            return redirect(url_for('users.index'))
        else:
            return render_template('users/edit.html', form=form, user=found_user)

    return render_template('users/show.html', user=found_user)
