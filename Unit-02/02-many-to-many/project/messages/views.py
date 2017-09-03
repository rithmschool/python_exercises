from flask import redirect, render_template, request, url_for,Blueprint, flash
from project.models import User, Message
from project.messages.forms import MessageForm
from project import db

messages_blueprint = Blueprint(
    'messages',
    __name__,
    template_folder='templates'
)


@messages_blueprint.route('/', methods=['GET', 'POST'])
def index(user_id):
  found_user = User.query.get_or_404(user_id)
  found_messages = Message.query.filter_by(user_id = found_user.id)

  if request.method == 'POST':
    form = MessageForm(request.form)
    if form.validate_on_submit():
      flash("New Message Added")
      new_msg = Message(request.form.get('message'), user_id)
      db.session.add(new_msg)
      db.session.commit()
      return redirect(url_for('messages.index', user_id = user_id))
    return render_template('messages/new.html', user=found_user, form=form)
  return render_template('messages/index.html', user=found_user, messages=found_messages)

@messages_blueprint.route('/new', methods=['POST', 'GET'])
def new(user_id):
  found_user = User.query.get_or_404(user_id)
  form = MessageForm()
  return render_template('messages/new.html', user=found_user, form=form)

@messages_blueprint.route('/<int:id>/edit')
def edit(user_id,id):
  found_user = User.query.get_or_404(user_id)
  found_message = Message.query.get_or_404(id)
  form = MessageForm(obj=found_message)

  return render_template('messages/edit.html', user=found_user, message=found_message, form=form)



@messages_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(user_id, id):
  found_message = Message.query.get_or_404(id)
  found_user = User.query.get_or_404(user_id)

  if request.method == b"PATCH":
    form = MessageForm(request.form)
    if form.validate():
      flash("Message Updated")
      found_message.message = request.form.get('message')
      db.session.add(found_message)
      db.session.commit()
      return redirect(url_for('messages.index', user_id = user_id))
    return render_template('messages/edit.html', user=found_user, message=found_message, form=form)

  if request.method == b"DELETE":
    flash("Message Deleted")
    db.session.delete(found_message)
    db.session.commit()
    return redirect(url_for('messages.index', user_id = user_id))
  return render_template('messages/show.html', message=found_message, user=found_user)



