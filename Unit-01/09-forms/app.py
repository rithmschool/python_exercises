from flask import Flask, render_template, redirect, url_for, request, abort
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
from forms import CreateUserForm, EditUserForm, DeleteUserForm, CreateMessageForm, EditMessageForm, DeleteMessageForm
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/fwitter'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
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
    users = User.query.all()
    if request.method == 'POST':
        form = CreateUserForm(request.form)
        if form.validate():
            user = User(request.form.get('username'), request.form.get('first_name'), request.form.get('last_name'), request.form.get('email'))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return render_template('users/new.html', form = form)

    return render_template('users/index.html', users = users)

@app.route('/new')
def new():
    form = CreateUserForm()        
    return render_template('users/new.html', form = form)

@app.route('/users/<id>', methods = ['GET','DELETE','PATCH'])
def show(id):
    user = User.query.get(id)
    if user == None:
        abort(404)

    if request.method == b'PATCH':
        edit_form = EditUserForm(request.form)
        if edit_form.validate():
            user.username = request.form.get('username')
            user.first_name = request.form.get('first_name')
            user.last_name = request.form.get('last_name')
            user.email = request.form.get('email')
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            delete_form = DeleteUserForm(request.form)
            return render_template('users/edit.html', edit_form = edit_form, delete_form = delete_form, user = user)

    if request.method == b'DELETE':
        delete_form = DeleteUserForm(request.form)
        if delete_form.validate():
            db.session.delete(user)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            edit_form = EditUserForm(obj = user)
            return render_template('users/edit.html', edit_form = edit_form, delete_form = delete_form, user = user)
    
    return render_template('users/show.html', user = user)

@app.route('/users/<id>/edit')
def edit(id):
    user = User.query.get(id)
    if user == None:
        abort(404)

    edit_form = EditUserForm(obj = user)
    delete_form = DeleteUserForm(obj = user)
    return render_template('users/edit.html', edit_form = edit_form, delete_form = delete_form, user = user)

# Messages routes

@app.route('/users/<user_id>/messages', methods = ['GET','POST'])
def index_message(user_id):
    user = User.query.get(user_id)
    if user == None:
        abort(404)

    if request.method == 'POST':
        form = CreateMessageForm(request.form)
        if form.validate():
            message = Message(request.form.get('text'), user.id)
            db.session.add(message)
            db.session.commit()
        else:
            return render_template('messages/new.html', user = user, form = form)

        return redirect(url_for('index_message', user_id = user.id))

    return render_template('messages/index.html', user = user)

@app.route('/users/<user_id>/messages/new')
def new_message(user_id):
    user = User.query.get(user_id)
    if user == None:
        abort(404)

    form = CreateMessageForm()
    return render_template('messages/new.html', user = user, form = form)

@app.route('/users/<user_id>/messages/<id>', methods = ['GET','PATCH','DELETE'])
def show_message(user_id, id):
    message = Message.query.get(id)
    if message == None:
        abort(404)
        
    if request.method == b'PATCH':
        edit_form = EditMessageForm(request.form)
        if edit_form.validate():
            message.text = request.form.get('text')
            db.session.add(message)
            db.session.commit()
            return redirect(url_for('index_message', user_id = user_id))
        else:
            delete_form = DeleteMessageForm(obj = message)
            return render_template('messages/edit.html', message = message, edit_form = edit_form, delete_form = delete_form)

    if request.method == b'DELETE':
        delete_form = DeleteMessageForm(request.form)
        if delete_form.validate():
            db.session.delete(message)
            db.session.commit()
            return redirect(url_for('index_message', user_id = user_id))
        else:
            edit_form = EditMessageForm(obj = message)
            return render_template('messages/edit.html', message = message, edit_form = edit_form, delete_form = delete_form)

    return render_template('messages/show.html', message = message)

@app.route('/users/<user_id>/messages/<id>/edit')
def edit_message(user_id, id):
    message = Message.query.get(id)
    if message == None:
        abort(404)

    edit_form = EditMessageForm(obj = message)
    delete_form = DeleteMessageForm(obj = message)
    return render_template('messages/edit.html', message = message, edit_form = edit_form, delete_form = delete_form)

# Errors!

@app.errorhandler(404)
def not_found(error = None):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug = True, port = 3333)
