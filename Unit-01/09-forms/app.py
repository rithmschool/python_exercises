from flask import Flask, redirect, request, url_for, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from forms import UserForm
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/messenger'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
modus = Modus(app)


class User(db.Model):
    __tablename__ = 'users'

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

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/users', methods=["GET", "POST"])
def index():
    form = UserForm(request.form)
    if request.method == "POST":
        if form.validate():
            db.session.add(User(request.form.get('username'), request.form.get('email'), request.form.get('first_name'), request.form.get('last_name')))
            db.session.commit()
            flash("You have successfully signed up!")
            return redirect(url_for('index'))
        else:
            return render_template('users/new.html', form=form)
    return render_template('users/index.html', users=User.query.all())

@app.route('/users/new')
def new():
    form = UserForm(request.form)
    return render_template('users/new.html', form=form)

@app.route('/users/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
    user_selected = User.query.get(id)
    form = UserForm(request.form)
    if request.method == b"PATCH":
        if form.validate_on_submit():
            db.session.add(User(request.form.get('username'), request.form.get('email'), request.form.get('first_name'), request.form.get('last_name')))
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return render_template('users/edit.html', form=form, user=user_selected)
    if request.method == b"DELETE":
        if form.validate_on_submit():
            db.session.delete(user_selected)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return render_template('users/show.html', form=form, user=user_selected)
    return render_template('users/show.html', form=form, user=user_selected)

@app.route('/users/<int:id>/edit')
def edit(id):
    user_selected = User.query.get(id)
    form = UserForm(obj=user_selected)
    return render_template('users/edit.html', form=form, user=user_selected)
if __name__ == '__main__':
    app.run(debug=True, port=3000)
