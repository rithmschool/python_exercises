from flask import Blueprint, request, redirect, render_template, url_for, flash
from project.messages.models import Message
from project.users.models import User
from project.messages.forms import DeleteForm, MessageForm
from project import db

messages_blueprint = Blueprint(
    'messages',
    __name__,
    template_folder='templates'
)

@messages_blueprint.route('/', methods=["GET", "POST"])
def index(user_id):
  delete_form = DeleteForm()
  if request.method == "POST":
    message_form = MessageForm(request.form)
    if message_form.validate():
      new_message = Message(request.form['content'], user_id)
      db.session.add(new_message)
      db.session.commit()
      flash("Message Created!")
      return redirect(url_for('messages.index', user_id=user_id))
    else:
      return render_template('messages/new.html', user=User.query.get(user_id), form=message_form)
  return render_template('messages/index.html', user=User.query.get(user_id), delete_form=delete_form)

@messages_blueprint.route('/new', methods=["GET", "POST"])
def new(user_id):
  message_form = MessageForm()
  return render_template('messages/new.html', user=User.query.get(user_id), form=message_form)

# Edit a message for a specific user
@messages_blueprint.route('/<int:id>/edit/')
def edit(user_id, id):
  found_message = Message.query.get(id)
  message_form = MessageForm(obj=found_message)
  return render_template('messages/edit.html', message=found_message, form=message_form)

# Delete a message for a specific user
@messages_blueprint.route('/<int:id>/', methods=["GET", "PATCH", "DELETE"])
def show(user_id, id):
  found_message = Message.query.get(id)
  if request.method == b"PATCH":
    message_form = MessageForm(request.form)
    if message_form.validate():
      found_message.content = message_form.content.data
      db.session.add(found_message)
      db.session.commit()
      flash("Message Updated!")
      return redirect(url_for('messages.index', user_id=user_id))
    return render_template('messages/edit.html', message=found_message, form=message_form)

  if request.method == b"DELETE":
    delete_form = DeleteForm(request.form)
    if delete_form.validate():
      db.session.delete(found_message)
      db.session.commit()
      flash("Message Deleted!")
    return redirect(url_for('messages.index', user_id=user_id))
  return render_template('messages/edit.html', message=found_message)

