from flask import Flask, url_for, redirect
from flask_sqlalchemy import SQLAlchemy 
from flask_modus import Modus 
import os

app = Flask(__name__)
modus = Modus(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/user-messages'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SECRET_KEY']=os.environ.get('SECRET_KEY')

from project.users.views import users_blueprint
app.register_blueprint(users_blueprint,url_prefix='/users')

from project.messages.views import messages_blueprint
app.register_blueprint(messages_blueprint, url_prefix='/users/<int:user_id>/messages')

@app.route('/')
def root():
	return redirect(url_for('users.index'))