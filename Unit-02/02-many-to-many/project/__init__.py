from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
import os
from flask_wtf.csrf import CsrfProtect # add csrf protection without creating a FlaskForm (for deleting)

app = Flask(__name__)
modus = Modus(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/many-many-example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)
csrf = CsrfProtect(app)

from project.employees.views import employees_blueprint
from project.departments.views import departments_blueprint

app.register_blueprint(departments_blueprint, url_prefix='/departments')
app.register_blueprint(employees_blueprint, url_prefix='/employees')


@app.route('/')
def root():
    return redirect('/employees')
