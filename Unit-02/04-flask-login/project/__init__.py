from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
modus = Modus(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/flask-sql-blueprints'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

db = SQLAlchemy(app)

# import a blueprint that we will create - Notice the placement of the import!
# it is essential that you do not import that blueprint before you initialize your app 
# and your db variable - this will cause errors with circular imports!
from project.users.views import users_blueprint
from project.messages.views import messages_blueprint
from project.tags.views import tags_blueprint

# register our blueprints with the application
app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(messages_blueprint, url_prefix='/users/<int:user_id>/messages')
app.register_blueprint(tags_blueprint, url_prefix='/tags')

# You also need to tell flask_login where it should redirect 
# someone to if they try to access a private route.
login_manager.login_view = 'users.login'

from project.models import User

# write a method with the user_loader decorator so that flask_login can find a current_user 
@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

@app.route('/')
def root():
    return redirect(url_for('users.login'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')