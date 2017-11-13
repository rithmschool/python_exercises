from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required
from project.users.models import User
from project.users.forms import CreateForm, EditForm, LoginForm
from project import db, bcrypt
from flask_wtf.csrf import validate_csrf
# from sqlalchemy.exc import IntegrityError

users_blueprint = Blueprint('users', __name__, template_folder='templates')

@users_blueprint.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        user = User.query.filter_by(username = request.form.get('username')).first()
        if form.validate_on_submit():
            if bcrypt.check_password_hash(user.password, request.form.get('password')):
                login_user(user)
                flash("You made it! You're logged in!")
                return redirect(url_for('users.index'))
            flash('You messed up, son!')

    return render_template('users/login.html', form = form)

@users_blueprint.route('/', methods = ['GET','POST'])
@login_required
def index():
    if request.method == 'POST':
        form = CreateForm(request.form)
        if form.validate():
            new_user = User(request.form['username'],
                            request.form['password'], 
                            request.form['first_name'],
                            request.form['last_name'],
                            request.form['email'])
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('users.index'))
        return render_template('users/new.html', form = form)
    return render_template('users/index.html', users = User.query.all())

@users_blueprint.route('/new')
@login_required
def new():
    return render_template('users/new.html', form = CreateForm())

@users_blueprint.route('/<int:id>', methods = ['GET','PATCH','DELETE'])
def show(id):
    user = User.query.get(id)
    if request.method == b'PATCH':
        form = EditForm(request.form)
        if form.validate():
            user.username = request.form.get('username')
            user.first_name = request.form.get('first_name')
            user.last_name = request.form.get('last_name')
            user.email = request.form.get('email')
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('users.index'))
        render_template('users/edit.html', user=user, form=form)

    if request.method == b'DELETE':
        if validate_csrf(request.form.get('csrf_token')) is None:
            db.session.delete(user)
            db.session.commit()
            return redirect(url_for('users.index'))    
    return render_template('users/show.html', user=user)

@users_blueprint.route('/<int:id>/edit')
@login_required
def edit(id):
    user = User.query.get(id)
    form = EditForm(obj=user)
    return render_template('users/edit.html', user=user, form=form)
