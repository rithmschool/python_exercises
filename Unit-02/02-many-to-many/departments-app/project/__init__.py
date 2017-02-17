from flask import Flask, redirect
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

import os

app = Flask(__name__, static_url_path='/static')
modus = Modus(app)
CsrfProtect(app)
bcrypt = Bcrypt(app)



# initialize the login_manager
login_manager = LoginManager()
# pass your app into the login_manager instance
login_manager.init_app(app)
login_manager.login_view = 'employees.login'



app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/departments_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "STRING"
app.config['TEMPLATES_AUTO_RELOAD'] = True

db = SQLAlchemy(app)


from project.employees.views import employees_blueprint
from project.messages.views import messages_blueprint


app.register_blueprint(employees_blueprint, url_prefix='/employees')
app.register_blueprint(messages_blueprint, url_prefix='/employees/<int:employee_id>/messages')





@app.route('/')
def root():
    return redirect('/employees')