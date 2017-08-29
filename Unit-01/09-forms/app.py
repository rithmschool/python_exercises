from flask import Flask, redirect, render_template, url_for, request, flash
from flask_modus import Modus 
from flask_sqlalchemy import SQLAlchemy
from forms import UserForm, MessageForm
from sqlalchemy.exc import IntegrityError

import os

app = Flask(__name__)
modus = Modus(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/users_messages'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
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
    form = UserForm(request.form)
    if request.method == 'POST':
        if form.validate():
            try:
                user = User(request.form['username'], request.form['email'], request.form['first_name'], request.form['last_name'])
                db.session.add(user)
                db.session.commit()
                flash("Successfully added user")  
                return redirect(url_for('index'))
            except IntegrityError as err:
                user_e = ""
                email_e = ""
                if "users_username_key" in str(err.orig.pgerror):
                    user_e = "This username has already been taken"
                if "users_email_key" in str(err.orig.pgerror):
                    email_e = "This email has already been registered"
                return render_template('users/new.html', form=form, user_e=user_e, email_e=email_e)
        else:
            e = "Please fix the error(s) above and try again"
            return render_template('users/new.html', form=form, e=e)

    return render_template('users/index.html', users=User.query.order_by(User.id))

@app.route('/users/new')
def new():
    form = UserForm(request.form)
    return render_template('users/new.html', form=form)

@app.route('/users/<int:id>', methods=['GET','PATCH','DELETE'])
def show(id):
    user = User.query.get_or_404(id)
    form = UserForm(request.form, obj=user)
    if request.method == b'PATCH':
        if form.validate():
            try:
                form.populate_obj(user)
                db.session.add(user)
                db.session.commit()
                flash("Successfully edited user information")
                return redirect(url_for('show', id=user.id))
            except IntegrityError as err:
                user_e = ""
                email_e = ""
                if "users_username_key" in str(err.orig.pgerror):
                    user_e = "This username has already been taken"
                if "users_email_key" in str(err.orig.pgerror):
                    email_e = "This email has already been registered"
                db.session.rollback()
                return render_template('users/edit.html', user=user, form=form, user_e=user_e, email_e=email_e)
        else:
            e = "Please fix the error(s) above and try again"
            return render_template('users/edit.html', user=user, form=form, e=e)
    if request.method == b'DELETE':
        db.session.delete(user)
        db.session.commit()
        flash("Sucessfully deleted user")
        return redirect(url_for('index'))
    return render_template('users/show.html', user=user)

@app.route('/users/<int:id>/edit')
def edit(id):
    user = User.query.get_or_404(id)
    form = UserForm(request.form, obj=user)
    return render_template('users/edit.html', user=user, form=form)

@app.route('/users/<int:user_id>/messages', methods=['GET', 'POST'])
def message_index(user_id):
    form = MessageForm(request.form)
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        if form.validate():
            message = Message(request.form['content'], user.id)
            db.session.add(message)
            db.session.commit()
            flash("Successfully added message")
            return redirect(url_for('message_index', user_id=user.id))
        else:
            e = "Please fix the error(s) above and try again"
            return render_template('messages/new.html', user=user, form=form, e=e)
    return render_template('messages/index.html', user=user, form=form)

@app.route('/users/<int:user_id>/messages/new')
def message_new(user_id):
    form = MessageForm(request.form)
    user = User.query.get_or_404(user_id)
    return render_template('messages/new.html', user=user, form=form)

@app.route('/users/<int:user_id>/messages/<int:message_id>', methods=['GET','PATCH','DELETE'])
def message_show(user_id, message_id):
    user = User.query.get_or_404(user_id)
    message = Message.query.get_or_404(message_id)
    form = MessageForm(request.form, obj=message)
    if request.method == b'PATCH':
        if form.validate():
            form.populate_obj(message)
            db.session.add(message)
            db.session.commit()
            flash("Successfully edited message")
            return redirect(url_for('message_show', user_id=user.id, message_id=message.id))
        else:
            e = "Please fix the error(s) above and try again"
            return render_template('messages/edit.html', user=user, message=message, form=form, e=e)
    if request.method == b'DELETE':
        db.session.delete(message)
        db.session.commit()
        flash("Sucessfully deleted message")
        return redirect(url_for('message_index', user_id=user.id))
    return render_template('messages/show.html', user=user, message=message)

@app.route('/users/<int:user_id>/messages/<int:message_id>/edit')
def message_edit(user_id, message_id):
    user = User.query.get_or_404(user_id)
    message = Message.query.get_or_404(message_id)
    form = MessageForm(request.form, obj=message)
    return render_template('messages/edit.html', user=user, message=message, form=form)

if os.environ.get('ENV') == 'production':
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

if __name__ == '__main__':
    app.run()