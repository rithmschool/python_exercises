from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
modus = Modus(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/fwitter'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

# Stupid jinja templates stopped auto-reloading, adding this to force them to.
app.jinja_env.auto_reload = True

from project.messages.models import Message
from project.users.views import users_blueprint
from project.messages.views import messages_blueprint

app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(messages_blueprint, url_prefix='/users/<int:user_id>/messages')

@app.route('/')
def root():
    return redirect(url_for('users.index'))

@app.route('/messages')
def messages():
    messages = Message.query.all()
    return render_template('messages.html', messages=messages)
