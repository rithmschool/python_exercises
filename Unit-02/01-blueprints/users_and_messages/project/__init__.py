from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
import os

app = Flask(__name__)
modus = Modus(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/users_forms_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)

from project.users.views import users_blueprint
from project.messages.views import messages_blueprint

app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(messages_blueprint, url_prefix='/users/<int:user_id>/messages')

@app.route('/')
def root():
		return "HELLO BLUEPRINTS!"


