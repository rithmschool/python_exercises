from flask import Flask
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
import os
from flask_wtf.csrf import CSRFProtect # add csrf protection without creating a FlaskForm (for deleting)

# create the Flask application object
app = Flask(__name__)
modus = Modus(app)


# set up the configuration for the app and initialize the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/flask-blueprints2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

# import the blueprints
from project.messages.views import messages_blueprint
from project.users.views import users_blueprint

# register the blueprints and set up the prefixes. these should include
#   ids passed if resource is built on top of another resource
app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(messages_blueprint, url_prefix='/users/<int:user_id>/messages')

@app.route('/')
def root():
    return "Where you trying to go?!"