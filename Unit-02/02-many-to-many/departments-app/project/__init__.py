from flask import Flask, redirect
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect
import os

app = Flask(__name__, static_url_path='/static')
modus = Modus(app)
CsrfProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/departments_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "STRING"
app.config['TEMPLATES_AUTO_RELOAD'] = True

db = SQLAlchemy(app)


from project.employees.views import employees_blueprint


app.register_blueprint(employees_blueprint, url_prefix='/employees')
#app.register_blueprint(messages_blueprint, url_prefix='/users/<int:user_id>/messages')

@app.route('/')
def root():
    return redirect('/employees')