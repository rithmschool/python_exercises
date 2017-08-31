from flask import Flask, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_bcrypt import Bcrypt
import os
from flask_login import LoginManager

app = Flask(__name__)
modus = Modus(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/user-messages'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SECRET_KEY']=os.environ.get('SECRET_KEY')


from project.models import Message, User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'
login_manager.login_message = 'Please log in'

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)

from project.users.views import users_blueprint
app.register_blueprint(users_blueprint,url_prefix='/users')

from project.messages.views import messages_blueprint
app.register_blueprint(messages_blueprint, url_prefix='/users/<int:user_id>/messages')

from project.tags.views import tags_blueprint
app.register_blueprint(tags_blueprint, url_prefix='/tags')

@app.route('/')
def root():
	return redirect(url_for('messages'))

@app.route('/messages')
def messages():
	message_list = Message.query.all()
	return render_template('messages/all.html', message_list=message_list)
