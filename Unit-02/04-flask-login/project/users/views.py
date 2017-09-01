from flask import redirect, request, render_template, Blueprint, url_for, flash
from project.models import User
from project.users.forms import UserForm, LoginForm, DeleteForm
from sqlalchemy.exc import IntegrityError
from project import db, bcrypt
from project.decorators import prevent_login_signup, ensure_correct_user
from flask_login import login_user, logout_user, login_required

# let's create the users_blueprint to register in our __init__.py
users_blueprint = Blueprint(
    'users',
    __name__,
    template_folder='templates'
)


# =============================================================================
# users routes
# =============================================================================
@login_required
@users_blueprint.route('/')
def index():
    return render_template('users/index.html', users=User.query.order_by(User.user_name).all())


@users_blueprint.route('/signup', methods=['GET', 'POST'])
@prevent_login_signup
def signup():
    form = UserForm(request.form)
    if request.method == 'POST':
        if form.validate():
            user_name = request.form.get('user_name')
            password = request.form.get('password')
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            email = request.form.get('email')

            new_user = User(user_name, password, first_name, last_name, email)
            db.session.add(new_user)

            try:
                db.session.commit()
                login_user(new_user)
                flash('User created!')
                return redirect(url_for('users.index'))
            except IntegrityError as err:
                flash('Username already exists.')
                return render_template('users/signup.html', form=form)

    return render_template('users/signup.html', form=form)


@users_blueprint.route('/login', methods=["GET", "POST"])
@prevent_login_signup
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        authenticated_user = User.authenticate(form.user_name.data, form.password.data)
        if authenticated_user:
            login_user(authenticated_user)
            flash('Login successful.')
            return redirect(url_for('users.index'))
        else:
            flash('Invalid login. Please try again.')
            return redirect(url_for('users.login'))
    return render_template('users/login.html', form=form)


@users_blueprint.route('/<int:id>/edit')
@login_required
@ensure_correct_user
def edit(id):
    found_user = User.query.get_or_404(id)
    form = UserForm(obj=found_user)
    return render_template('users/edit.html', form=form, user=found_user)


@users_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
@login_required
@ensure_correct_user
def show(id):
    found_user = User.query.get_or_404(id)
    if request.method == b'PATCH':
        form = UserForm(request.form)
        if form.validate():
            found_user.user_name = request.form.get('user_name')
            found_user.password = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
            found_user.first_name = request.form.get('first_name')
            found_user.last_name = request.form.get('last_name')
            found_user.email = request.form.get('email')

            db.session.add(found_user)
            db.session.commit()

            return redirect(url_for('users.index'))

        return render_template('users/edit.html', form=form, user=found_user)
    if request.method == b'DELETE':
        form = DeleteForm(request.form)
        if form.validate():
            db.session.delete(found_user)
            db.session.commit()
            logout_user()
            flash('User Deleted')
            return redirect(url_for('users.login'))
        return render_template('users/edit.html', form=form, user=found_user)

    return render_template('users/show.html', user=found_user)


@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out.')
    return redirect(url_for('users.login'))
