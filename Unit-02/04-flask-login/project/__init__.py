from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy 
from flask_modus import Modus 
from flask_bcrypt import Bcrypt
from os import environ
from flask_login import LoginManager

app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/users-messages'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
modus=Modus(app)
db=SQLAlchemy(app)

from project.users.views import users_blueprint
from project.messages.views import messages_blueprint
from project.tags.views import tags_blueprint

app.register_blueprint(users_blueprint, url_prefix = '/users')
app.register_blueprint(messages_blueprint, url_prefix = '/users/<int:user_id>/messages')
app.register_blueprint(tags_blueprint, url_prefix = '/tags')

login_manager.login_view = 'users.login'

from project.users.models import User
from project.messages.models import Message


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

@app.route('/')
def root():
	return redirect(url_for('users.index'))

@app.route('/messages')
def messages():
	messages = Message.query.all()
	return render_template('messages.html', messages = messages)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('users/404.html', e=e), 404