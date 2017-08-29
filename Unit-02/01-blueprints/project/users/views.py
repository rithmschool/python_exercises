from flask import redirect, render_template, request, url_for, Blueprint, flash, abort
from project.users.models import User
from project.users.forms import NewUser
from flask_wtf.csrf import validate_csrf, ValidationError # we will need this to validate CSRF for deleting an owner
from project import db

users_blueprint = Blueprint(
    'users',
    __name__,
    template_folder = 'templates'
)

@users_blueprint.route('/', methods=['GET', 'POST'])
def index():
    form = NewUser(request.form)
    if request.method == 'POST':
      if form.validate() == True:
          user = User(form.username.data, form.email.data, 
            form.first_name.data, form.last_name.data, form.image_url.data)
          db.session.add(user)
          db.session.commit()

          flash("User Created!")
          return redirect(url_for('users.index'))
      else:
          return render_template('users/new.html', form=form)
    
    users = User.query.order_by(User.id)
    return render_template('users/index.html', users = users)

@users_blueprint.route('/new')
def new():
    form = NewUser(request.form)
    return render_template('users/new.html', form=form)

@users_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):
    user = User.query.get(id)
    if user is None:
        abort(404)

    if (request.method == b'PATCH'):
        form = NewUser(request.form)
        user.username = form.username.data
        user.email = form.email.data, 
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.image_url = form.image_url.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.index'))

    if (request.method == b'DELETE'):
        try: # validate_csrf will raise an error if the token does not match so we need to catch it using try/except
            validate_csrf(request.form.get('csrf_token'))   
        except ValidationError: # if someome tampers with the CSRF token when we delete an owner
            return redirect(url_for('users.show', id=id))

        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('users.index'))
    return render_template('users/show.html', user=user)

@users_blueprint.route('/<int:id>/edit')
def edit(id):
    user = User.query.get(id)
    if user is None:
        abort(404)

    form = NewUser(obj=user)
    return render_template('users/edit.html', id=user.id, form=form)