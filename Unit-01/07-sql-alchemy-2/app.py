from flask import Flask, render_template, redirect, url_for, request, abort
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/fwitter'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
modus = Modus(app)

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.Text)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    email = db.Column(db.Text)
    messages = db.relationship('Message', backref='user', lazy='dynamic')

    def __init__(self, username, first_name, last_name, email):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __repr__(self):
        return "User: id - {}".format(self.id)

class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, text, user_id):
        self.text = text;
        self.user_id = user_id;

    def __repr__(self):
        return "Message: id - {}".format(self.id)

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/users', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        user = User(request.form.get('username'), request.form.get('first_name'), request.form.get('last_name'), request.form.get('email'))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))

    users = User.query.all()
    return render_template('users/index.html', users = users)

@app.route('/new')
def new():
    return render_template('users/new.html')

@app.route('/users/<id>', methods = ['GET','DELETE','PATCH'])
def show(id):
    user = User.query.get(id)
    if request.method == b'PATCH':
        user.username = request.form.get('username')
        user.first_name = request.form.get('first_name')
        user.last_name = request.form.get('last_name')
        user.email = request.form.get('email')
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))

    if request.method == b'DELETE':
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('index')) 
    
    return render_template('users/show.html', user = user)

@app.route('/users/<id>/edit')
def edit(id):
    user = User.query.get(id)
    return render_template('users/edit.html', user = user)

# Messages routes

@app.route('/users/<user_id>/messages', methods = ['GET','POST'])
def index_message(user_id):
    user = User.query.get(user_id)
    if user == None:
        abort(404)

    if request.method == 'POST':
        message = Message(request.form.get('text'), user.id)
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('index_message', user_id = user.id))

    return render_template('messages/index.html', user = user)

@app.route('/users/<user_id>/messages/new')
def new_message(user_id):
    user = User.query.get(user_id)
    return render_template('messages/new.html', user = user)

@app.route('/users/<user_id>/messages/<id>', methods = ['GET','PATCH','DELETE'])
def show_message(user_id, id):
    message = Message.query.get(id)
    if message == None:
        abort(404)
        
    if request.method == b'PATCH':
        message.text = request.form.get('text')
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('index_message', user_id = user_id))

    if request.method == b'DELETE':
        db.session.delete(message)
        db.session.commit()
        return redirect(url_for('index_message', user_id = user_id))

    return render_template('messages/show.html', message = message)

@app.route('/users/<user_id>/messages/<id>/edit')
def edit_message(user_id, id):
    message = Message.query.get(id)
    return render_template('messages/edit.html', message = message)

# Errors!

@app.errorhandler(404)
def not_found(error = None):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug = True, port = 3333)
