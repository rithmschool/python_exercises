from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
modus = Modus(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/07-sql-alchemy-2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):

    __tablename__ = "users"

    # id, username, email, first_name, last_name
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
        return "{} {}'s' username is {} and email is {}.".format(self.first_name, self.last_name, self.username, self.email)

@app.route('/users', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_user = User(request.form['username'], request.form['email'], request.form['first_name'], request.form['last_name'])
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))

    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/users/new')
def new():
    return render_template('new.html')

@app.route('/users/<int:user_id>', methods=["GET","PATCH","DELETE"])
def show(user_id):
    found_user = User.query.get_or_404(user_id)

    if request.method == b"PATCH":
        found_user.username = request.form['username']
        found_user.email = request.form['email']
        found_user.first_name = request.form['first_name']
        found_user.last_name = request.form['last_name']
        db.session.add(found_user)
        db.session.commit()
        return redirect(url_for('index'))

    if request.method == b"DELETE":
        db.session.delete(found_user)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('show.html', user=found_user)


@app.route('/users/<int:user_id>/edit')
def edit(user_id):
    found_user = User.query.get_or_404(user_id)
    return render_template('edit.html', user=found_user)

if __name__ == '__main__':
    app.run(debug=True,port=3000)