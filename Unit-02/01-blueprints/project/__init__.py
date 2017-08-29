from flask import Flask
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
modus = Modus(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/blue-owners'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)

# import blueprints
from project.owners.views import owners_blueprint
from project.histories.views import histories_blueprint

# register blueprints with the app
app.register_blueprint(owners_blueprint, url_prefix='/owners')
app.register_blueprint(histories_blueprint, url_prefix='/owners/<int:owner_id>/histories')

@app.route('/')
def root():
    # from IPython import embed; embed()
    from IPython import embed; embed()
    return "Welcome to the root directory!"