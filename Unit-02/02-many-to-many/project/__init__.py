from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
import os

app = Flask(__name__)
modus = Modus(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/manymany'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)

# import a blueprint that we will create
from project.employees.views import employees_blueprint
from project.departments.views import departments_blueprint

# register our blueprints with the application
app.register_blueprint(employees_blueprint, url_prefix='/employees')
app.register_blueprint(departments_blueprint, url_prefix='/departments')

@app.route('/')
def root():
    return redirect('/employees')