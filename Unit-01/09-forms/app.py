from flask import Flask, request, redirect, render_template, url_for, flash, abort
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
import os
from forms import NewUser, NewMessage

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
    image_url = db.Column(db.Text)

    def __init__(self, username, email, first_name, last_name, image_url):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.image_url = image_url

    def __repr__(self):
        return "Username: {}, Email: {}, First: {}, Last: {}".format(self.username, self.email, self.first_name, self.last_name)

class Message(db.Model):

    __tablename__ = "messages"

    #create the essential columns for our table
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)
    user_id = db.Column(db.Integer)

    def __init__(self, message, user_id):
        self.message = message
        self.user_id = user_id

    def __repr__(self):
        return "Message by user {}: {}".format(self.user_id, self.message)

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/users', methods=['GET', 'POST'])
def index():
    form = NewUser(request.form)
    if request.method == 'POST':
      if form.validate() == True:
          user = User(form.username.data, form.email.data, 
            form.first_name.data, form.last_name.data, form.image_url.data)
          db.session.add(user)
          db.session.commit()

          flash("New User Created!")
          return redirect(url_for('index'))
      else:
          return render_template('users/new.html', form=form)
    
    users = User.query.order_by(User.id)
    return render_template('users/index.html', users = users)

@app.route('/users/new')
def new():
    form = NewUser(request.form)
    return render_template('users/new.html', form=form)

@app.route('/users/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):
    user = User.query.get(id)
    if user is None:
        abort(404)

    if (request.method == b'PATCH'):
        form = NewUser(request.form)
        user.username = form.username.data
        user.email = form.email.data, 
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.image_url = form.image_url.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))

    if (request.method == b'DELETE'):
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('users/show.html', user=user)

@app.route('/users/<int:id>/edit')
def edit(id):
    user = User.query.get(id)
    if user is None:
        abort(404)

    form = NewUser(obj=user)
    return render_template('users/edit.html', id=user.id, form=form)

@app.route('/users/<int:user_id>/messages', methods=['GET', 'POST'])
def index_messages(user_id):
    form = NewMessage(request.form)
    username = User.query.get(user_id).username
    if username is None:
        abort(404)

    if request.method == 'POST':
      if form.validate() == True:
          user_message = Message(form.message.data, user_id)
          db.session.add(user_message)
          db.session.commit()
          flash("New Message Created!")
          return redirect(url_for('index_messages', user_id=user_id))
      else:
          return render_template('messages/new.html', user_id=user_id, form=form)

    user_messages = Message.query.filter(Message.user_id == user_id).all()
    
    return render_template('messages/index.html', user_id=user_id, username=username, user_messages=user_messages)

@app.route('/users/<int:user_id>/messages/new')
def new_message(user_id):
    form = NewMessage(request.form)
    return render_template('messages/new.html', user_id=user_id, form=form)

@app.route('/users/<int:user_id>/messages/<int:message_id>/edit')
def edit_messages(user_id, message_id):
    message = Message.query.get(message_id)
    if message is None:
        abort(404)

    form = NewMessage(obj=message)
    return render_template('messages/edit.html', user_id=user_id, message_id=message.id, form=form)

@app.route('/users/<int:user_id>/messages/<int:message_id>/show', methods=['GET', 'PATCH', 'DELETE'])
def show_message(user_id, message_id):
    message = Message.query.get(message_id)
    if message is None:
        abort(404)

    if (request.method == b'PATCH'):
        form = NewMessage(request.form)
        message.message = form.message.data
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('index_messages', user_id=user_id))

    if (request.method == b'DELETE'):
        db.session.delete(message)
        db.session.commit()
        return redirect(url_for('index_messages', user_id=user_id))
    return render_template('messages/show.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)













