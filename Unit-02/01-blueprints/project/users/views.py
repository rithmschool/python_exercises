from flask import redirect, render_template, request, url_for, flash, Blueprint
from project import db
from project.users.models import User
from project.users.forms import UserForm
from sqlalchemy.exc import IntegrityError
from flask_wtf.csrf import validate_csrf, ValidationError

users_blueprint = Blueprint(
    'users',
    __name__,
    template_folder='templates'
)

@users_blueprint.route('/', methods=['GET','POST'])
def index():
    form = UserForm(request.form)
    if request.method == 'POST':
        if form.validate():
            try:
                user = User(request.form['username'], request.form['email'], request.form['first_name'], request.form['last_name'])
                db.session.add(user)
                db.session.commit()
                flash("Hola")  
                return redirect(url_for('users.index'))
            
            except IntegrityError as err:
                user_e = ""
                email_e = ""
                if "users_username_key" in str(err.orig.pgerror):
                    user_e = "Username is already in use, please login instead"
                if "users_email_key" in str(err.orig.pgerror):
                    email_e = "Email already being used"
                return render_template('users/new.html', form=form, user_e=user_e, email_e=email_e)
        else:
            error = "Please fix the error(s) above"
            return render_template('users/new.html', form=form, error=error)

    return render_template('users/index.html', users=User.query.order_by(User.id))

@users_blueprint.route('/new')
def new():
    form = UserForm(request.form)
    return render_template('users/new.html', form=form)

@users_blueprint.route('/<int:user_id>', methods=['GET','PATCH','DELETE'])
def show(user_id):
    user = User.query.get_or_404(user_id)
    form = UserForm(request.form, obj=user)
    if request.method == b'PATCH':
        if form.validate():
            try:
                form.populate_obj(user)
                db.session.add(user)
                db.session.commit()
                flash("Successfully updated info")
                return redirect(url_for('users.show', user_id=user.id))
            except IntegrityError as err:
                user_e = ""
                email_e = ""
                if "users_username_key" in str(err.orig.pgerror):
                    user_e = "Username unavailable"
                if "users_email_key" in str(err.orig.pgerror):
                    email_e = "Email has already in use"
                db.session.rollback()
                return render_template('users/edit.html', user=user, form=form, user_e=user_e, email_e=email_e)
        else:
            e = "Please fix the error(s) above and try again"
            return render_template('users/edit.html', user=user, form=form, e=e)
    if request.method == b'DELETE':
        try:
            validate_csrf(request.form.get('csrf_token'))
        except ValidationError:
            delete_e = "There was a problem deleting this user"
            return render_template('users/show.html', user=user, delete_e=delete_e)
        db.session.delete(user)
        db.session.commit()
        flash("Deleted user")
        return redirect(url_for('users.index'))
    return render_template('users/show.html', user=user)

@users_blueprint.route('/<int:user_id>/edit')
def edit(user_id):
    user = User.query.get_or_404(user_id)
    form = UserForm(request.form, obj=user)
    return render_template('users/edit.html', user=user, form=form)

