from flask import redirect, request, render_template, Blueprint, url_for
from project.users.models import User
from project.messages.models import Message
from project.messages.forms import MessageForm
from project import db

# let's create the messages_blueprint to register in our __init__.py
messages_blueprint = Blueprint(
    'messages',
    __name__,
    template_folder='templates'
)


@messages_blueprint.route('/', methods=['GET', 'POST'])
def index(user_id):
    if request.method == 'POST':
        form = MessageForm(request.form)
        if form.validate():
            message = request.form.get('message')

            db.session.add(Message(message, user_id))
            db.session.commit()

            return redirect(url_for('messages.index', user_id=user_id))
        else:
            return render_template('messages/new.html', form=form, user_id=user_id)
    else:  
        user = User.query.get(user_id)
        messages = user.messages.all()

        return render_template('messages/index.html', user=user, messages=messages)    


@messages_blueprint.route('/<int:msg_id>/edit')
def edit(user_id, msg_id):
    found_message = Message.query.get_or_404(msg_id)
    form = MessageForm(obj=found_message)
    return render_template('messages/edit.html', form=form, msg=found_message)


@messages_blueprint.route('/new')
def new(user_id):
    form = MessageForm(request.form)
    return render_template('messages/new.html', form=form, user_id=user_id)


@messages_blueprint.route('/show/<int:msg_id>', methods=['GET', 'PATCH', 'DELETE'])
def show(user_id, msg_id):
    found_message = Message.query.get_or_404(msg_id)
    if request.method == b'PATCH':
        found_message.message = request.form.get('message')

        db.session.add(found_message)
        db.session.commit()

        return redirect(url_for('messages.index', user_id=user_id))

    if request.method == b'DELETE':
        db.session.delete(found_message)
        db.session.commit()

        return redirect(url_for('messages.index', user_id=user_id))

    return render_template('messages/show.html', msg=found_message)