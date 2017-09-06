from flask import Flask, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask import render_template
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
modus = Modus(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login"
login_manager.login_message = "Please log in!"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/flask-blueprints'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

from project.users.views import users_blueprint
from project.messages.views import messages_blueprint
from project.tags.views import tags_blueprint

# register our blueprints with the application
app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(messages_blueprint, url_prefix='/users/<int:user_id>/messages')
app.register_blueprint(tags_blueprint, url_prefix='/tags')

from project.messages.models import Message
from project.users.models import User
from flask_login import current_user


@app.route('/')
def root():
	if(current_user.is_authenticated):
		return redirect(url_for('users.show', id=current_user.id))
	else:
		return redirect(url_for('users.login'))

@app.route('/messages')
def all():
	return render_template('messages/all.html', messages=Message.query.order_by(Message.text).all())

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)