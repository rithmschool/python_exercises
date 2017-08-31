from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from flask_modus import Modus
from flask_wtf.csrf import CsrfProtect # add csrf protection without creating a FlaskForm (for deleting)


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/learn-auth'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'super secret' # bad practice in general, but we'll live with it for now
db = SQLAlchemy(app)
modus = Modus(app)
csrf = CsrfProtect(app)


from project.users.views import users_blueprint

app.register_blueprint(users_blueprint, url_prefix='/users')