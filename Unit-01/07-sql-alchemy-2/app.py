from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy #step 1: pip install flask_sqlalchemy psycopg2
from flask_modus import Modus




app = Flask(__name__)
#step 2: app.config to cofig to correct database
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://localhost/flask-user-app"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
modus = Modus(app)
db = SQLAlchemy(app)


#set up our table
class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Message(db.Model):

    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id



@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/users', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_user = User(request.form['first_name'], request.form['last_name'])  # name from type in new.html#
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('users/index.html', users=User.query.all())



@app.route('/users/new')
def new():
    return render_template('users/new.html')

@app.route('/users/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
    found_user = User.query.get(id)

    if request.method == b"PATCH":
        found_user.first_name = request.form['first_name']
        found_user.last_name = request.form['last_name']
        db.session.add(found_user)
        db.session.commit()
        return redirect(url_for('index'))

    if request.method == b"DELETE":
        db.session.delete(found_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('users/show.html', user=found_user)

    return render_template('users/show.html', user=found_user)

@app.route('/users/<int:id>/edit')
def edit(id):
    #refactored using a list comprehension
    found_user = User.query.get(id)
    return render_template('users/edit.html', user=found_user)



@app.route('/users/<int:id>/messages', methods=["GET", "POST"])
def messages_index(user_id):
    if request.method == "POST":
        new_message = Message(request.form['content'], user_id)
        db.session.add(new_message)
        db.commit()
        return redirect(url_for('messages_index', user_id=user_id))
    return render_template('messages/index.html', user=User.query.get(user_id))

@app.route('/users/<int:id>/messages/new')
def messages_new(user_id):
    return render_template('messages/new.html', user=User.query.get(user_id))

@app.route('/users/<int:id>/messages/<int:id>', methods=['GET', 'POST', 'DELETE'])
def messages_show(user_id, id):
    found_message = Message.query.get(id)

    if request.method == b'PATCH':
        found_message.content = request.form['content']





if __name__ == '__main__':
    app.run(debug=True, port=3000)
