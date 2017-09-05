from flask import Flask, request, redirect, url_for, render_template, flash
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
# from forms import UserForm, MessageForm
from forms import MessageForm
import os


### Flask Form #####
from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/message-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
modus = Modus(app)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

class User(db.Model):
  __tablename__ = "users"

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.Text)
  firstname = db.Column(db.Text)
  lastname = db.Column(db.Text)
  email = db.Column(db.Text)
  img_url = db.Column(db.Text)
  messages = db.relationship('Message', backref='user', lazy='dynamic')

  def __init__(self, username, email, firstname, lastname, img_url):
    self.username = username
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

###### Form Validation ######
def validators_unique(form, field):
# Check if item is in table --> https://stackoverflow.com/questions/44650699/flask-sqlalchemy-check-if-object-exist-in-db
# How to use variable in filter_by --> https://stackoverflow.com/questions/19506105/flask-sqlalchemy-query-with-keyword-as-variable
# Access user friendly label name --> https://www.reddit.com/r/flask/comments/3u59rx/wtforms_label_field/.
  kwargs = {field.name : field.data}
  if User.query.filter_by(**kwargs).count() > 0:
    raise ValidationError('Please select another ' + field.label.text.lower())

class UserForm(FlaskForm):
  username = StringField('User Name', [validators.Length(min=3), validators_unique])
  email = StringField('E-mail', [validators.Email(), validators_unique])
  firstname = StringField('First Name', [validators.Length(min=1)])
  lastname = StringField('Last Name', [validators.Length(min=1)])
  img_url = StringField('Image URL', [validators.URL(require_tld=False, message='Invalid URL or incomplete URL.')])

###### End Form Validation ######


###### USER Routes.  ######
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
            request.form.get('username'),\
            request.form.get('email'), \
            request.form.get('firstname'),\
            request.form.get('lastname'), \
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

  if request.method == b"PATCH":
    if form.validate():
      flash("Update Successful")
      found_user.username = request.form.get('username')
      found_user.email = request.form.get('email')
      found_user.firstname = request.form.get('firstname')
      found_user.lastname = request.form.get('lastname')
      found_user.img_url = request.form.get('img_url')
      db.session.add(found_user)
      db.session.commit()
      return redirect(url_for('index'))
    else:
      return render_template('user/edit.html', users=found_user, form=form)

  if request.method == b"DELETE":
    flash("User Deleted")
    db.session.delete(found_user)
    db.session.commit()
    return redirect(url_for('index'))

  return render_template('user/show.html', users=found_user)


#################################################
### Messages ###
################
@app.route('/users/<int:user_id>/messages')
def index_message(user_id):
  found_user = User.query.get(user_id)
  found_message = Message.query.filter_by(user_id = found_user.id)
  return render_template('message/index.html', user=found_user, messages = found_message)


@app.route('/users/<int:user_id>/messages/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show_message(user_id, id):

  found_message = Message.query.get_or_404(id)
  found_user = User.query.get_or_404(user_id)
  form = MessageForm(request.form)

  if request.method == b"PATCH":
    if form.validate():
      flash("Message Updated")
      found_message.message = request.form.get('message')
      db.session.add(found_message)
      db.session.commit()
      return redirect(url_for('index_message', user_id = user_id))
    else:
      return render_template('message/edit.html', user=found_user, message=found_message, form=form)

  if request.method == b"DELETE":
    flash("Message Deleted")
    db.session.delete(found_message)
    db.session.commit()
    return redirect(url_for('index_message', user_id = user_id))

  return render_template('message/show.html', message=found_message, user=found_user)


@app.route('/users/<int:user_id>/messages/<int:id>/edit')
def edit_message(user_id,id):
  found_user = User.query.get_or_404(user_id)
  found_message = Message.query.get_or_404(id)
  form = MessageForm(obj=found_message)
  # if not found_user or not found_message or not found_message.user_id == user_id:
  #   return render_template('message/404.html')

  return render_template('message/edit.html', user=found_user, message=found_message, form=form)

@app.route('/users/<int:user_id>/messages/new', methods=['POST', 'GET'])
def new_message(user_id):
    found_user = User.query.get_or_404(user_id)
    form = MessageForm(request.form)

    if request.method == 'POST':
      if form.validate_on_submit():
        flash("New Message Added")
        new_msg = Message(request.form.get('message'), user_id)
        db.session.add(new_msg)
        db.session.commit()
        return redirect(url_for('index_message', user_id = user_id))
    return render_template('message/new.html', user=found_user, form=form)


if __name__ == '__main__':
    app.run(debug=True,port=3000)
































