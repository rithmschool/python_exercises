from flask import redirect, render_template, request, url_for, flash,Blueprint
from project.messages.forms import MessageForm, DeleteForm
from project.models import Message,User
from project import db
from project.decorators import ensure_authenticated, ensure_correct_user
messages_blueprint = Blueprint(
  'messages',
  __name__,
  template_folder='templates'
  )

@messages_blueprint.route('/', methods =["GET", "POST"])
@ensure_authenticated
def index(user_id):
    user = User.query.get(user_id)
    if request.method == "POST":
        form = MessageForm(request.form)
        if form.validate():
            new_message = Message(form.content.data, user.id)
            db.session.add(new_message)
            db.session.commit()
            flash('Message Created!')
            return redirect(url_for('messages.index', user_id=user.id))
        return render_template('messages/new.html', form=form, user=user)
    return render_template('messages/index.html', user=user)


@messages_blueprint.route('/new', methods=["GET", "POST"])
@ensure_authenticated
@ensure_correct_user
def new(user_id):
  form = MessageForm()
  return render_template('messages/new.html', user=User.query.get(user_id), form=form)

@messages_blueprint.route('/<int:id>/edit')
@ensure_authenticated
@ensure_correct_user
def edit(user_id, id):
  found_message = Message.query.get(id)
  form = MessageForm(obj=found_message)
  return render_template('messages/edit.html', message=found_message, form=form)


@messages_blueprint.route('/<int:id>', methods=["GET", "PATCH", "DELETE"])
@ensure_authenticated
@ensure_correct_user
def show(user_id, id):
  found_message = Message.query.get(id)
  if request.method == b"PATCH":
    form = MessageForm(request.form)
    if form.validate():
      found_message.content = request.form['content']
      db.session.add(found_message)
      db.session.commit()
      flash('Message Updated!')
      return redirect(url_for('messages.index', user_id=user_id))
    return render_template('messages/edit.html', message=found_message, form=form)
  if request.method == b"DELETE":
    delete_form = DeleteForm(request.form)
    if delete_form.validate():
      db.session.delete(found_message)
      db.session.commit()
      flash('Message Deleted!')
    return redirect(url_for('messages.index', user_id=user_id))
  return render_template('messages/show.html', message=found_message)