from flask import Flask, url_for, redirect
from os import environ
from modus import Modus
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/02-many-to-many'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
modus = Modus(app)
db = SQLAlchemy(app)

