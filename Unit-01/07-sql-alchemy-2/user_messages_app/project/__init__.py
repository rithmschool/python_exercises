from flask import Flask, redirect
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect
import os

app = Flask(__name__, static_url_path='/static')
modus = Modus(app)
CsrfProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/users_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "STRING"
app.config['TEMPLATES_AUTO_RELOAD'] = True

db = SQLAlchemy(app)


from project.users.views import users_blueprint
from project.messages.views import messages_blueprint

app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(messages_blueprint, url_prefix='/users/<int:user_id>/messages')

@app.route('/')
def root():
    return redirect('/users')