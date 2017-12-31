from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy #step 1: pip install flask_sqlalchemy psycopg2
from flask_modus import Modus
import os




app = Flask(__name__)
#step 2: app.config to cofig to correct database
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://localhost/flask-user-app"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
modus = Modus(app)
db = SQLAlchemy(app)

from project.users.views import users_blueprint
from project.messages.views import messages_blueprint

app.register_blueprint(users_blueprint, url_prefix='/users')
app.regiester_blueprint(messages_blueprint, url_prefix='/users/<int:user_id>/messages')



@app.route('/')
def root():
    return redirect(url_for('users.index'))
