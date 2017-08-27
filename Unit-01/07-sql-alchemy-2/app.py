from flask import Flask, request, redirect, url_for, render_template, flash
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
from forms import UserForm
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/message-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
modus = Modus(app)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

class User(db.Model):
  __tablename__ = "users"

  id = db.Column(db.Integer, primary_key=True)
  firstname = db.Column(db.Text)
  lastname = db.Column(db.Text)
  email = db.Column(db.Text)
  img_url = db.Column(db.Text)
  messages = db.relationship('Message', backref='user', lazy='dynamic')

  def __init__(self, firstname, lastname, email, img_url):
    self.firstname = firstname
    self.lastname = lastname
    self.email = email
    self.img_url = img_url

  def __repr__(self):
    return "Name {} {} email {} image URL {}".format(self.first, self.last, self.email, self.image_url)

class Message(db.Model):
  __tablename__ = "messages"

  id = db.Column(db.Integer, primary_key=True)
  message = db.Column(db.Text)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  def __init__(self, message, user_id):
    self.message = message
    self.user_id = user_id

  def __repr__(self):
    return "The message is ' {} '' and user id is {}".format(self.message, self.user_id)



############
## Routes ##
############

@app.route('/')
def root():
  return redirect(url_for('index'))

@app.route('/users', methods=['POST', 'GET'])
def index():
  return render_template('user/index.html', users=User.query.all(), messages=Message.query.all())

@app.route('/users/signup', methods=['GET','POST'])
def signup():
    form = UserForm(request.form)
    if request.method == 'POST':
      if form.validate_on_submit():
        flash("You have succesfully signed up!")
        db.session.add(User( \
            request.form.get('firstname'),\
            request.form.get('lastname'), \
            request.form.get('email'), \
            request.form.get('img_url')))
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('user/signup.html', form=form)

@app.route('/users/<int:id>/edit')
def edit(id):
  found_user = User.query.get_or_404(id)
  form = UserForm(obj=found_user)



  return render_template('user/edit.html', users=found_user, form=form)

@app.route('/users/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):

  found_user = User.query.get_or_404(id)
  form = UserForm(request.form)

  if not found_user:
    return render_template('404.html')

  if request.method == b"PATCH":
    if form.validate():
      flash("Update Successful")
      # form.populate_obj(found_user)
      found_user.firstname = request.form.get('firstname')
      found_user.lastname = request.form.get('lastname')
      found_user.email = request.form.get('email')
      found_user.img_url = request.form.get('img_url')
      db.session.add(found_user)
      db.session.commit()
      return redirect(url_for('index'))
    else:
      return render_template('user/edit.html', users=found_user, form=form)

  if request.method == b"DELETE":
    flash("User Deleted Successful")
    db.session.delete(found_user)
    db.session.commit()
    return redirect(url_for('index'))

  return render_template('user/show.html', users=found_user)




#################################################
### Messages ###
################
@app.route('/users/<int:user_id>/messages', methods=['POST', 'GET'])
def index_message(user_id):
  found_user = User.query.get(user_id)
  if request.method == 'POST':
    db.session.add(Message(request.form.get('title'), user_id))
    db.session.commit()
    return redirect(url_for('index_message', user_id=found_user.id))
  return render_template('message/index.html', user=found_user)


@app.route('/users/<int:user_id>/messages/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show_message(user_id, id):

  found_message = Message.query.get(id)
  found_user = User.query.get(user_id)

  if not found_message:
    return render_template('404.html')

  if request.method == b"PATCH":
    found_message.title = request.form.get('title')
    db.session.add(found_message)
    db.session.commit()
    return redirect(url_for('index_message', user_id=user_id))

  if request.method == b"DELETE":
    db.session.delete(found_message)
    db.session.commit()
    return redirect(url_for('index_message', user_id=user_id))

  return render_template('message/show.html', messages=found_message, user=found_user)

@app.route('/user/<int:user_id>/messages/<int:id>/edit')
def edit_message(user_id,id):
  found_user = User.query.get(user_id)
  found_message = Message.query.get(id)

  if not found_user or not found_message or not found_message.user_id == user_id:
    return render_template('message/404.html')

  return render_template('message/edit.html', user=found_user, message=found_message)

@app.route('/user/<int:user_id>/messages/new')
def new_message(user_id):
    found_user = User.query.get(user_id)
    return render_template('message/new.html', user= found_user)



if __name__ == '__main__':
    app.run(debug=True,port=3000)