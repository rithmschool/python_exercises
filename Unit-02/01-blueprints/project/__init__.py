from flask import Flask, redirect, url_for
from flask_modus import Modus 
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect # add csrf protection without creating a FlaskForm (for deleting) 

import os

app = Flask(__name__)
modus = Modus(app)
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/users_messages'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)

from project.users.views import users_blueprint
from project.messages.views import messages_blueprint

app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(messages_blueprint, url_prefix='/users/<int:user_id>/messages')

@app.route('/')
def root():
    return redirect(url_for('users.index'))


if os.environ.get('ENV') == 'production':
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')
