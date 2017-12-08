from flask import redirect, url_for, flash
from functools import wraps
from flask_login import current_user 

def ensure_correct_user(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        correct_id = kwargs.get('user_id') or kwargs.get('id')
        if correct_id != current_user.id:
            flash("Not Authorized, fren.")
            return redirect(url_for('users.welcome'))
        return fn(*args, **kwargs)
    return wrapper       
