from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy #step 1: pip install flask_sqlalchemy psycopg2
from flask_modus import Modus
from forms import UserForm, MessageForm, DeleteForm
import os




app = Flask(__name__)
#step 2: app.config to cofig to correct database
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://localhost/flask-user-app"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
modus = Modus(app)
db = SQLAlchemy(app)

from project.users.views import users_blueprint
from project.messages.views import messages_blueprint

app.register_blueprint(users_blueprint, url_prefix='/owners')
app.regiester_blueprint(messages_blueprint, url_prefix='/messages')



@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/users', methods=["GET", "POST"])
def index():
    delete_form = DeleteForm()
    if request.method == "POST":
        form = UserForm(request.form)
        if form.validate():
            new_user = User(request.form['first_name'], request.form['last_name'])  # name from type in new.html#
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return render_template('users/new.html', form=form)
    return render_template('users/index.html', users=User.query.all(), delete_form=delete_form)



@app.route('/users/new')
def new():
    user_form = UserForm()
    return render_template('users/new.html', form=user_form)



@app.route('/users/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
    found_user = User.query.get(id)

    if request.method == b"PATCH":
        form = UserForm(request.form)
        if form.validate():
            found_user.first_name = form.first_name.data
            found_user.last_name = form.last_name.data
            db.session.add(found_user)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('users/edit.html', user=found_user, form=form)

    if request.method == b"DELETE":
        delete_form = DeleteForm(request.form)
        if delete_form.validate():
            db.session.delete(found_user)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('users/show.html', user=found_user)


@app.route('/users/<int:id>/edit')
def edit(id):
    #refactored using a list comprehension
    found_user = User.query.get(id)
    user_form = UserForm(obj=found_user) #do not use request.form, use obj= to prepopulate the form
    return render_template('users/edit.html', user=found_user, form=user_form)




@app.route('/users/<int:user_id>/messages', methods=["GET", "POST"])
def messages_index(user_id):
    delete_form = DeleteForm()
    if request.method == "POST":
        message_form = MessageForm(request.form)
        if message_form.validate():
            new_message = Message(request.form['content'], user_id)
            db.session.add(new_message)
            db.session.commit()
            return redirect(url_for('messages_index', user_id=user_id, form=message_form))
        else:
            return render_template('messages/new.html', user=User.query.get(user_id), form=message_form)
    return render_template('messages/index.html', user=User.query.get(user_id), delete_form=delete_form)

@app.route('/users/<int:user_id>/messages/new')
def messages_new(user_id):
    message_form = MessageForm(request.form)
    return render_template('messages/new.html', user=User.query.get(user_id), form=message_form)

@app.route('/users/<int:user_id>/messages/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def messages_show(user_id, id):
    found_message = Message.query.get(id)

    if request.method == b'PATCH':
        message_form = MessageForm(request.form)
        if message_form.validate():
            found_message.content = request.form['content']
            db.session.add(found_message)
            db.session.commit()
            return redirect(url_for('messages_index', user_id=user_id))
        return render_template('messages/edit.html', message=found_message, form=message_form)

    elif request.method == b'DELETE':
        delete_form = DeleteForm(request.form)
        if delete_form.validate():
            db.session.delete(found_message)
            db.session.commit()
        return redirect(url_for('messages_index', user_id=user_id))
    return render_template('messages/show.html', message=found_message, form=message_form)

@app.route('/users/<int:user_id>/messages/<int:id>/edit')
def messages_edit(user_id, id):
    found_message = Message.query.get(id)
    message_form = MessageForm(obj=found_message)
    return render_template('messages/edit.html', message=found_message, form=message_form)
