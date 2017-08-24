from flask import Flask, render_template, redirect, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from forms import UserForm, MessageForm
from sqlalchemy.exc import IntegrityError
import os

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/flask-sql-alchemy2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

db = SQLAlchemy(app)

modus = Modus(app)


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.Text, unique=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    email = db.Column(db.Text, unique=True)
    messages = db.relationship('Message', cascade="all, delete-orphan", backref='user', lazy='dynamic')

    def __init__(self, user_name, first_name, last_name, email):
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __repr__(self):
        return "User {} {}'s user name is {}".format(self.first_name, self.last_name,
                                                        self.user_name)

class Message(db.Model):

    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, message, user_id):
        self.message = message
        self.user_id = user_id


@app.route('/')
def root():
    return redirect(url_for('index'))


# =============================================================================
# routes for users
# =============================================================================
@app.route('/users', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = UserForm(request.form)
        if form.validate():
            user_name = request.form.get('user_name')
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            email = request.form.get('email')

            db.session.add(User(user_name, first_name, last_name, email))

            try:
                db.session.commit()
            except IntegrityError as err:
                print(err)
                return render_template('users/new.html', form=form)

            return redirect(url_for('index'))
        else:
            return render_template('users/new.html', form=form)
    return render_template('users/index.html', users=User.query.order_by(User.user_name).all())


@app.route('/users/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):
    found_user = User.query.get_or_404(id)
    if request.method == b'PATCH':
        form = UserForm(request.form)
        if form.validate():
            found_user.user_name = request.form.get('user_name')
            found_user.first_name = request.form.get('first_name')
            found_user.last_name = request.form.get('last_name')
            found_user.email = request.form.get('email')

            db.session.add(found_user)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return render_template('users/edit.html', form=form)
    if request.method == b'DELETE':
        db.session.delete(found_user)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('users/show.html', user=found_user)


@app.route('/users/<int:id>/edit')
def edit(id):
    found_user = User.query.get_or_404(id)
    form = UserForm(obj=found_user)
    return render_template('users/edit.html', form=form, user=found_user)


@app.route('/users/new')
def new():
    form = UserForm(request.form)
    return render_template('users/new.html', form=form)

# =============================================================================
# routes for messages
# =============================================================================
@app.route('/users/<int:user_id>/messages', methods=['GET', 'POST'])
def message_index(user_id):
    if request.method == 'POST':
        form = MessageForm(request.form)
        if form.validate():
            message = request.form.get('message')

            db.session.add(Message(message, user_id))
            db.session.commit()

            return redirect(url_for('message_index', user_id=user_id))
        else:
            return render_template('messages/new.html', form=form, user_id=user_id)
    else:  
        user = User.query.get(user_id)
        messages = user.messages.all()

        return render_template('messages/index.html', user=user, messages=messages)


@app.route('/users/<int:user_id>/messages/show/<int:msg_id>', methods=['GET', 'PATCH', 'DELETE'])
def message_show(user_id, msg_id):
    found_message = Message.query.get_or_404(msg_id)
    if request.method == b'PATCH':
        found_message.message = request.form.get('message')

        db.session.add(found_message)
        db.session.commit()

        return redirect(url_for('message_index', user_id=user_id))

    if request.method == b'DELETE':
        db.session.delete(found_message)
        db.session.commit()

        return redirect(url_for('message_index', user_id=user_id))

    return render_template('messages/show.html', msg=found_message)


@app.route('/users/<int:user_id>/messages/<int:msg_id>/edit')
def message_edit(user_id, msg_id):
    found_message = Message.query.get_or_404(msg_id)
    form = MessageForm(obj=found_message)
    return render_template('messages/edit.html', form=form, msg=found_message)


@app.route('/users/<int:user_id>/messages/new')
def message_new(user_id):
    form = MessageForm(request.form)
    return render_template('messages/new.html', form=form, user_id=user_id)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if os.environ.get('ENV') == 'production':
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

if __name__ == '__main__':
    app.run()
