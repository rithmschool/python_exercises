from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
import jinja2

app = Flask(__name__)
modus = Modus(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/user-sql-alchemy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.jinja_env.undefined = jinja2.StrictUndefined
app.jinja_env.auto_reload = True

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    email = db.Column(db.Text)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    messages = db.relationship('Message', backref='user', lazy='dynamic')

    def __init__(self, username, email, first_name, last_name):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
    
    def __repr__(self):
        return "Username: {}, email: {}, first name: {}, last name: {}".format(self.username, self.email, self.first_name, self.last_name)

@app.route('/users', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        db.session.add(User(request.form['username'], request.form['email'], request.form['first_name'], request.form['last_name']))
        db.session.commit()
        return redirect(url_for('/users/index'))
    return render_template('/users/index.html', users=User.query.all())

@app.route('/users/new')
def new():
    return render_template('/users/new.html')

@app.route('/users/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
    if request.method == b"PATCH":
        update_user = User.query.get(id)
        update_user.username = request.form['username']
        update_user.email = request.form['email']
        update_user.first_name = request.form['first_name']
        update_user.last_name = request.form['last_name']
        db.session.add(update_user)
        db.session.commit()
        return redirect(url_for('/users/index'))
    
    if request.method == b"DELETE":
        delete_user = User.query.get(id)
        db.session.delete(delete_user)
        db.session.commit()
        return redirect(url_for('/users/index'))
    
    user = User.query.filter_by(id=id).first_or_404()
    return render_template('/users/show.html', user=user)

@app.route('/users/<int:id>/edit')
def edit(id):
    return render_template('/users/edit.html', user=User.query.get(id))



class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.VARCHAR(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, text, user_id):
        self.text = text
        self.user_id = user_id
    
    def __repr__(self):
        return "{} wrote text: {}, user_id: {}".format(self.users.username, self.text, self.user_id)

@app.route('/users/<int:id>/messages', methods=["GET", "POST"])
def m_index(id):
    check_user = User.query.filter_by(id=id).first_or_404()
    if request.method == "POST":
        db.session.add(Message(request.form['message'], request.form['user_id']))
        db.session.commit()
        return redirect(url_for('m_index', id=check_user.id, messages=check_user.messages))
    return render_template('/messages/index.html', id=check_user.id, messages=check_user.messages)

@app.route('/users/<int:id>/messages/new')
def m_new(id):
    check_user = User.query.filter_by(id=id).first_or_404()
    return render_template('/messages/new.html', id=check_user.id)

@app.route('/users/<int:id>/messages/<int:mid>', methods=["GET", "PATCH", "DELETE"])
def m_show(id, mid):
    check_user = User.query.filter_by(id=id).first_or_404()
    check_message = Message.query.filter_by(id=mid).first_or_404()
    if request.method == b"PATCH":
        update_message = check_message
        update_message.text = request.form['message']
        update_message.user_id = request.form['user_id']
        db.session.add(update_message)
        db.session.commit()
        return redirect(url_for('m_index', id=check_user.id))
    
    if request.method == b"DELETE":
        delete_message = check_message
        db.session.delete(delete_message)
        db.session.commit()
        return redirect(url_for('m_index', id=check_user.id))

    return render_template('/messages/show.html', id=check_user.id, message=check_message)

@app.route('/users/<int:id>/messages/<int:mid>/edit')
def m_edit(id, mid):
    check_user = User.query.filter_by(id=id).first_or_404()
    check_message = Message.query.filter_by(id=mid).first_or_404()
    return render_template('/messages/edit.html', id=check_user.id, message=check_message)


if __name__ == '__main__':
    app.run(port=3000, debug=True)