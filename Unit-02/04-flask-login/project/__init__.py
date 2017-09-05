from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/flask-login'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bcrypt = Bcrypt(app)
modus = Modus(app)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'
login_manager.login_message = 'Please log in!'


from project.models import User

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)


from project.users.views import users_blueprint
app.register_blueprint(users_blueprint, url_prefix='/users')

from project.messages.views import messages_blueprint
app.register_blueprint(messages_blueprint, url_prefix='/users/<int:user_id>/messages')

from project.tags.views import tags_blueprint
app.register_blueprint(tags_blueprint, url_prefix='/tags')

@app.route('/')
def root():
    return "HELLO BLUEPRINTS!"

