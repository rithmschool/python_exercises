from flask import redirect, render_template, request, url_for,Blueprint, flash
from project.models import User, Message, Tag
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
  message = Message.query.get(id)
  tags = [tag.id for tag in message.tags]
  form = MessageForm(tags=tags)
  form.set_choices()
  return render_template('messages/edit.html', user=found_user, form=form, message = message)

@messages_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(user_id, id):
  found_message = Message.query.get_or_404(id)
  found_user = User.query.get_or_404(user_id)

  if request.method == b"PATCH":
    form = MessageForm(request.form)
    form.set_choices()
    if form.validate():
      flash("Message Updated")
      found_message.message = form.message.data
      found_message.tags = []
      for tag in form.tags.data:
        found_message.tags.append(Tag.query.get(tag))
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



