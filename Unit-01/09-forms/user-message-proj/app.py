##flask-sql-alchemy is my virtenv
from flask import Flask,render_template,url_for,request,redirect
from flask_modus import Modus 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
modus = Modus(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

