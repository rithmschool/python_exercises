from flask import Flask, redirect, url_for
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager 
import os

app = Flask(__name__)
modus = Modus(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/user-message-auth'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'top secret'
db = SQLAlchemy(app)


from project.users.views import users_blueprint
from project.messages.views import messages_blueprint

app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(messages_blueprint, url_prefix='/users/<int:user_id>/messages')

login_manager.login_view = 'users.login'

from project.users.models import User 

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.route('/')
def root():
	return redirect(url_for('users.login'))

if __name__ == '__main__':
	app.run(debug=True)	