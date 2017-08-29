from flask import Flask, redirect, render_template, url_for, request
from flask_modus import Modus 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
modus = Modus(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/users_messages'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    messages = db.relationship('Message', backref='user', cascade="all, delete-orphan", lazy='dynamic')

    def __init__(self, username, email, first_name, last_name):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return "Username: {}, Email: {}, First Name: {}, Last Name: {}".format(self.username, self.email, self.first_name, self.last_name)

class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.VARCHAR(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return self.content


@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/users', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        user = User(request.form['username'], request.form['email'], request.form['first_name'], request.form['last_name'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('users/index.html', users=User.query.all())

@app.route('/users/new')
def new():
    return render_template('users/new.html')

@app.route('/users/<int:id>', methods=['GET','PATCH','DELETE'])
def show(id):
    user = User.query.get_or_404(id)
    if request.method == b'PATCH':
        user.username = request.form['username']
        user.email = request.form['email']
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    if request.method == b'DELETE':
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('users/show.html', user=user)

@app.route('/users/<int:id>/edit')
def edit(id):
    user = User.query.get_or_404(id)
    return render_template('users/edit.html', user=user)

@app.route('/users/<int:user_id>/messages', methods=['GET', 'POST'])
def message_index(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        message = Message(request.form['content'], user.id)
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('message_index', user_id=user.id))
    return render_template('messages/index.html', user=user)

@app.route('/users/<int:user_id>/messages/new')
def message_new(user_id):
    user = User.query.get(user_id)
    return render_template('messages/new.html', user=user)

@app.route('/users/<int:user_id>/messages/<int:message_id>', methods=['GET','PATCH','DELETE'])
def message_show(user_id, message_id):
    message = Message.query.get_or_404(message_id)
    if request.method == b'PATCH':
        message.content = request.form['content']
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('message_index', user_id=user_id))
    if request.method == b'DELETE':
        db.session.delete(message)
        db.session.commit()
        return redirect(url_for('message_index', user_id=user_id))
    return render_template('messages/show.html', message=message)

@app.route('/users/<int:user_id>/messages/<int:message_id>/edit')
def message_edit(user_id, message_id):
    message = Message.query.get_or_404(message_id)
    return render_template('messages/edit.html', message=message)

if __name__ == '__main__':
    app.run(debug=True, port=3000)