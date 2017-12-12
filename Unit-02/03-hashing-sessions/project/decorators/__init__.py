from functools import wraps
from flask import redirect, url_for, session, flash

def ensure_authenticated(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not session.get('user_id'):
            flash("Please log in first")
            return redirect(url_for('users.login'))
        return fn(*args, **kwargs)
    return wrapper

def prevent_login_signup(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if session.get('user_id'):
            flash("You are logged in already")
            return redirect(url_for('users.index'))
        return fn(*args, **kwargs)
    return wrapper

def ensure_correct_user(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        correct_id = kwargs.get('user_id') or kwargs.get('id')
        if correct_id != session.get('user_id'):
            flash("Not Authorized")
            return redirect(url_for('users.index',id=session.get('user_id')))
        return fn(*args, **kwargs)
    return wrapper