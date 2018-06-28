from functools import wraps
from flask import redirect, url_for, session, flash

def ensure_authenticated(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		if session.get('user_id') is None:
			flash('Please log in first!')
			return redirect(url_for('users.login'))
		return fn(*args, **kwargs)
	return wrapper

def prevent_loginsignup(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		if session.get('user_id'):
			flash('You are logged in already!')
			return redirect(url_for('users.index'))
		return fn(*args, **kwargs)
	return wrapper

def ensure_correct_user(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		correct_id = kwargs.get('id')
		if correct_id != session.get('user_id'):
			flash('Not Authorized')
			return redirect(url_for('users.index'))
		return fn(*args, **kwargs)
	return wrapper

def ensure_correct_user_message(fn):
	@wraps(fn)
	def wrapper(*args, ** kwargs):
		correct_id = kwargs.get('id')
		if correct_id != session.get('id'):
			flash('Not Authortized')
			return redirect(url_for('users.index'))
		return fn(*args, **kwargs)
	return wrapper

