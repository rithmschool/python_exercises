from flask import Flask, request, redirect, render_template, url_for, flash
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
import os
from forms import NewUser

# create the Flask application object
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/flask-forms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
# create the database object
modus = Modus(app)
db = SQLAlchemy(app)

class User(db.Model):

    __tablename__ = "users"

    # create the essential columns for our table
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
        return "Username: {}, Email: {}, First: {}, Last: {}".format(self.username, self.email, self.first_name, self.last_name)

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/users', methods=['GET', 'POST'])
def index():
    form = NewUser(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data, 
          form.first_name.data, form.last_name.data)
        db.session.add(user)
        db.session.commit()

        from IPython import embed; embed()

        flash("New User Created!")
        return redirect(url_for('index'))
    
    users = User.query.order_by(User.id)
    return render_template('index.html', users = users)

@app.route('/users/new')
def new():
    form = NewUser(request.form)
    return render_template('new.html', form=form)

@app.route('/users/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):
    user = User.query.get(id)
    
    if (request.method == b'PATCH'):
        form = NewUser(request.form)
        user.username = form.username.data
        user.email = form.email.data, 
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))

    if (request.method == b'DELETE'):
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('show.html', user=user)

@app.route('/users/<int:id>/edit')
def edit(id):
    #UNABLE TO POPULATE FORM WITH PRIOR DATA!
    user = User.query.get(id)
    form = NewUser(obj=user)
    return render_template('edit.html', id=user.id, form=form)

if __name__ == '__main__':
    app.run(debug=True)
