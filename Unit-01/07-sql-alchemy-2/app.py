from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
import jinja2

app = Flask(__name__)
modus = Modus(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/user-sql-alchemy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.jinja_env.undefined = jinja2.StrictUndefined
app.jinja_env.auto_reload = True

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    email = db.Column(db.Text)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)

    def __init__(self, username, email, first_name, last_name):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
    
    def __repr__(self):
        return "Username: {}, email: {}, first name: {}, last name: {}".format(self.username, self.email, self.first_name, self.last_name)

@app.route('/users', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        db.session.add(User(request.form['username'], request.form['email'], request.form['first_name'], request.form['last_name']))
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', users=User.query.all())

@app.route('/users/new')
def new():
    return render_template('new.html')

@app.route('/snacks/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
    if request.method == b"PATCH":
        update_user = User.query.get(id)
        update_user.username = request.form['username']
        update_user.email = request.form['email']
        update_user.first_name = request.form['first_name']
        update_user.last_name = request.form['last_name']
        db.session.add(update_user)
        db.session.commit()
        return redirect(url_for('index'))
    
    if request.method == b"DELETE":
        delete_user = User.query.get(id)
        db.session.delete(delete_user)
        db.session.commit()
        return redirect(url_for('index'))
    
    user = User.query.filter_by(id=id).first_or_404()
    return render_template('show.html', user=user)

@app.route('/snacks/<int:id>/edit')
def edit(id):
    return render_template('edit.html', user=User.query.get(id))

if __name__ == '__main__':
    app.run(port=3000, debug=True)