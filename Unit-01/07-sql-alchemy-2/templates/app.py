from flask import Flask,request,redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy 
from flask_modus import Modus 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://localhost/users-messages"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
modus = Modus(app)
db = SQLAlchemy(app)

class User(db.Model):
	
	__tablename__ = 'users'

	id = db.Column(db.Integer,primary_key = True)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)

	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name




if __name__ == '__main__':
	app.run(debug=True,port=3000)