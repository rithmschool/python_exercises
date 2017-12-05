from flask import Flask, url_for, redirect
from os import environ
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/02-many-to-many'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = environ.get('SECRET_KEY') or "hi"
modus = Modus(app)
db = SQLAlchemy(app)

from project.departments.views import departments_blueprint
from project.employees.views import employees_blueprint

app.register_blueprint(departments_blueprint, url_prefix="/departments")
app.register_blueprint(employees_blueprint, url_prefix="/employees")

app.route('/')
def root():
	return "hello"