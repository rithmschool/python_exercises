from flask import Flask, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
#from forms import UserForm, MessageFrom, DeleteForm
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/flask-blueprints'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
modus = Modus(app)
db = SQLAlchemy(app)

# import a blueprint that we will create
from project.users.views import users_blueprint
from project.messages.views import messages_blueprint

# register our blueprints with the application
app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(messages_blueprint, url_prefix='/users/<int:user_id>/messages')


@app.route('/')
def root():
    return redirect(url_for('users.index'))
