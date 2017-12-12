from flask import redirect, render_template, request, url_for, flash,Blueprint,session,g
from project.users.forms import UserForm, DeleteForm, LoginForm
from project.models import User
from project import db,bcrypt
from sqlalchemy.exc import IntegrityError
from project.decorators import ensure_authenticated, prevent_login_signup, ensure_correct_user

users_blueprint = Blueprint(
  'users',
  __name__,
  template_folder='templates'
  )
@users_blueprint.before_request
def current_user():
    if session.get('user_id'):
        g.current_user = User.query.get(session['user_id'])
    else:
        g.current_user = None

@users_blueprint.route('/')
@ensure_authenticated
def index():
  delete_form = DeleteForm()
  return render_template('users/index.html',users=User.query.all(),delete_form=delete_form)

@users_blueprint.route('/', methods = ['POST'])
@prevent_login_signup
def signup():
  
  
    form = UserForm(request.form)
    if form.validate():
      try:
       new_user = User(
        form.first_name.data, 
        form.last_name.data,
        form.username.data,
        form.password.data)
       db.session.add(new_user)
       db.session.commit()
       session['user_id'] = new_user.id
       flash('User Created!')
       return redirect(url_for('users.index'))
      except IntegrityError:
        flash('Username already taken!')
        return render_template('users/new.html', form=form)
  
      return render_template('users/new.html', form=form)
  


@users_blueprint.route('/login',methods = ['GET','POST'])
@prevent_login_signup
def login():
  form = LoginForm(request.form)
  if request.method == 'POST':
    if form.validate():
      authenticated_user = User.authenticate(form.username.data,form.password.data)
      if authenticated_user:
        session['user_id'] = authenticated_user.id
        flash('You are Logged in')
        return redirect(url_for('users.index'))
      else:
        flash('Invalid Credentials')
        return redirect(url_for('users.login'))
  return render_template('users/login.html',form = form)


@users_blueprint.route('/new')
@prevent_login_signup
def new():

	user_form = UserForm()
	return render_template('users/new.html',form = user_form)


@users_blueprint.route('/<int:id>/edit')
@ensure_correct_user
@ensure_authenticated	
def edit(id):
	found_user = User.query.get(id)
	user_form = UserForm(obj=found_user)
	
	return render_template('users/edit.html', user = found_user, form=user_form)

@users_blueprint.route('/<int:id>',methods = ['GET','PATCH','DELETE'])
@ensure_authenticated 	
@ensure_correct_user
def show(id):
  found_user = User.query.get(id)
  if request.method == b"PATCH":
    form = UserForm(request.form)
    if form.validate(): 
      found_user.first_name = form.first_name.data
      found_user.last_name = form.last_name.data
      db.session.add(found_user)
      db.session.commit()
      flash('User Updated!')
      return redirect(url_for('users.index'))
    return render_template('users/edit.html', user=found_user, form=form)
  if request.method == b"DELETE":
    delete_form = DeleteForm(request.form)
    if delete_form.validate():
      db.session.delete(found_user)
      db.session.commit()
      flash('User Deleted!')
    return redirect(url_for('users.index'))
  return render_template('users/show.html', user=found_user)


@users_blueprint.route('/logout')
@ensure_authenticated
def logout():
  session.pop('user_id')
  flash('Logged out!')
  return redirect(url_for('users.login'))