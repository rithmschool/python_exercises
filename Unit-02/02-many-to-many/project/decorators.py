from functools import wraps
from flask import render_template, flash
from flask_login import current_user

def ensure_correct_user(fn):
  @wraps(fn)
  def wrapper(*args, **kwargs):
    if kwargs.get('id') is not None and kwargs.get('id') != current_user.id:
      flash("Not Authorized")
      return render_template('users/not_auth.html')
    elif kwargs.get('user_id') is not None and kwargs.get('user_id') != current_user.id:
      flash("Not Authorized")
      return render_template('users/not_auth.html')
    return fn(*args, **kwargs)
  return wrapper

def ensure_correct_message_user(fn):
  @wraps(fn)
  def wrapper(*args, **kwargs):
    if kwargs.get('user_id') is not None and kwargs.get('user_id') != current_user.id:
      flash("Not Authorized")
      return render_template('users/not_auth.html')
    return fn(*args, **kwargs)
  return wrapper