from flask import redirect, render_template, request, url_for, Blueprint, flash, abort
from project.messages.models import Message
from project.users.models import User
from project.messages.forms import NewMessage
from flask_wtf.csrf import validate_csrf, ValidationError # we will need this to validate CSRF for deleting an owner
from project import db

# blueprint for the message resource, registered in __init__.py
messages_blueprint = Blueprint(
    'messages',
    __name__,
    template_folder='templates'
)

@messages_blueprint.route('/', methods=['GET', 'POST'])
def index(user_id):
    form = NewMessage(request.form)
    username = User.query.get(user_id).username
    if username is None:
        abort(404)

    if request.method == 'POST':
      if form.validate() == True:
          user_message = Message(form.message.data, user_id)
          db.session.add(user_message)
          db.session.commit()
          flash("Message Created!")
          return redirect(url_for('messages.index', user_id=user_id))
      else:
          return render_template('messages/new.html', user_id=user_id, form=form)

    user_messages = Message.query.filter(Message.user_id == user_id).all()
    
    return render_template('messages/index.html', user_id=user_id, username=username, user_messages=user_messages)

@messages_blueprint.route('/new')
def new(user_id):
    form = NewMessage(request.form)
    return render_template('messages/new.html', user_id=user_id, form=form)

@messages_blueprint.route('/<int:message_id>/edit')
def edit(user_id, message_id):
    message = Message.query.get(message_id)
    if message is None:
        abort(404)

    form = NewMessage(obj=message)
    return render_template('messages/edit.html', user_id=user_id, message_id=message.id, form=form)

@messages_blueprint.route('/<int:message_id>/show', methods=['GET', 'PATCH', 'DELETE'])
def show(user_id, message_id):
    message = Message.query.get(message_id)
    if message is None:
        abort(404)

    if (request.method == b'PATCH'):
        form = NewMessage(request.form)
        message.message = form.message.data
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('messages.index', user_id=user_id))

    if (request.method == b'DELETE'):
        try: # validate_csrf will raise an error if the token does not match so we need to catch it using try/except
            validate_csrf(request.form.get('csrf_token'))   
        except ValidationError: # if someome tampers with the CSRF token when we delete an owner
            return redirect(url_for('messages.show', user_id=user_id, message_id=message_id))

        db.session.delete(message)
        db.session.commit()
        return redirect(url_for('messages.index', user_id=user_id))
    return render_template('messages/show.html', message=message)








