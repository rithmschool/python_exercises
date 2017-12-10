from functools import wraps
from flask import redirect, url_for, session, flash
from flask_login import current_user

# def ensure_authenticated(fn):
# 	@wraps(fn)
# 	def wrapper(*args, **kwargs):
# 		if session.get('user_id') is None:
# 			flash('Please log in first!')
# 			return redirect(url_for('users.login'))
# 		return fn(*args,**kwargs)
# 	return wrapper

def prevent_login_signup(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		if current_user.is_authenticated:
			flash('You are logged in already')
			return redirect(url_for('users.index'))
		return fn(*args, **kwargs)
	return wrapper

def ensure_correct_user(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		correct_id = kwargs.get('id') or kwargs.get('user_id')
		if correct_id != current_user.id:
			flash('Not Authorized')
			return redirect(url_for('users.index', id=current_user.id))
		return fn(*args, **kwargs)
	return wrapper