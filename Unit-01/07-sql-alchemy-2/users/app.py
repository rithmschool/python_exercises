# we will need users
# users can have many messages
# need a 1 to many relationship in the DB
# create users, create relationship with messages
# create CRUD operations for users and messages
# create a form for each using WTForms
# which will need environment variables to prevent CSRF attacks
# deploy to heroku: need to do conditional logic for dev vs. prod envs

from flask import Flask, redirect, render_template, url_for, flash, request
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
# from forms import 
import os

app = Flask(__name__)

@app.route('/')
def root():
	pass

@app.route('/users')
def index_users():
	pass

@app.route('/users/new')
def new_user():
	pass

@app.route('/users/<int:user_id>')
def show_user():
	pass

@app.route('/users/<int:user_id>/edit')
def edit_user():
	pass

@app.route('/users/<int:user_id>/messages')
def index_messages():
	pass

@app.route('/users/<int:user_id>/messages/new')
def new_message():
	pass

@app.route('/users/<int:user_id>/messages/<int:message_id>')
def show_message():
	pass

@app.route('/users/<int:user_id>/messages/<int:message_id>/edit')
def edit_message():
	pass


if __name__ == "__main__":
	app.run(debug=True,port=3000)