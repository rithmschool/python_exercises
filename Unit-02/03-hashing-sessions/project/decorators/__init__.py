from flask import redirect, url_for, flash, session
from functools import wraps

def ensure_logged_in(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not session.get('user_id'):
            flash("Please log in first, fren.")
            return redirect(url_for('users.login'))
        return fn(*args, **kwargs)
    return wrapper 

def ensure_correct_user(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if (kwargs.get('user_id') or kwargs.get('id')) != session.get('user_id'):
            flash("Not Authorized, fren.")
            return redirect(url_for('users.welcome'))
        return fn(*args, **kwargs)
    return wrapper       
