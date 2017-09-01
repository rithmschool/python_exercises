from flask import redirect, request, render_template, Blueprint, url_for, flash, session
from project.models import User
from project.users.forms import UserForm, LoginForm, DeleteForm
from sqlalchemy.exc import IntegrityError
from project import db, bcrypt
from project.decorators import ensure_authenticated, prevent_login_signup, ensure_correct_user

# let's create the users_blueprint to register in our __init__.py
users_blueprint = Blueprint(
    'users',
    __name__,
    template_folder='templates'
)


# =============================================================================
# users routes
# =============================================================================
@users_blueprint.route('/')
@ensure_authenticated
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
                session['user_id'] = new_user.id
                flash('User created!')
                return redirect(url_for('users.index'))
            except IntegrityError as err:
                flash('Username already taken')
                return render_template('users/signup.html', form=form)


    return render_template('users/signup.html', form=form)


@users_blueprint.route('/login', methods=["GET", "POST"])
@prevent_login_signup
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        authenticated_user = User.authenticate(form.user_name.data, form.password.data)
        if authenticated_user:
            session['user_id'] = authenticated_user.id
            flash('Login successful.')
            return redirect(url_for('users.index'))
        else:
            flash('Invalid login. Please try again.')
            return redirect(url_for('users.login'))
    return render_template('users/login.html', form=form)


@users_blueprint.route('/<int:id>/edit')
@ensure_authenticated
@ensure_correct_user
def edit(id):
    found_user = User.query.get_or_404(id)
    form = UserForm(obj=found_user)
    return render_template('users/edit.html', form=form, user=found_user)


@users_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
@ensure_authenticated
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
            session.pop('user_id')
            flash('User Deleted')
            return redirect(url_for('users.login'))
        return render_template('users/edit.html', form=form, user=found_user)

    return render_template('users/show.html', user=found_user)


@users_blueprint.route('/logout')
@ensure_authenticated
def logout():
    session.pop('user_id')
    flash('You have successfully logged out.')
    return redirect(url_for('users.login'))
