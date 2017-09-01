from flask import redirect, request, render_template, Blueprint, url_for, flash
from project.models import User, Message, Tag
from project.messages.forms import MessageForm, DeleteForm
from project import db
from project.decorators import ensure_authenticated, ensure_correct_user

# let's create the messages_blueprint to register in our __init__.py
messages_blueprint = Blueprint(
    'messages',
    __name__,
    template_folder='templates'
)


@messages_blueprint.route('/', methods=['GET', 'POST'])
@ensure_authenticated
def index(user_id):
    if request.method == 'POST':
        form = MessageForm(request.form)
        form.set_choices()
        if form.validate():
            new_message = Message(form.message.data, user_id)
            for tag in form.tags.data:
                new_message.tags.append(Tag.query.get(tag))
            db.session.add(new_message)
            db.session.commit()

            flash('New message added.')

            return redirect(url_for('messages.index', user_id=user_id))
        else:
            return render_template('messages/new.html', form=form, user_id=user_id)
    else:  
        user = User.query.get(user_id)
        messages = user.messages.all()

        return render_template('messages/index.html', user=user, messages=messages)    


@messages_blueprint.route('/<int:msg_id>/edit')
@ensure_authenticated
@ensure_correct_user
def edit(user_id, msg_id):
    found_message = Message.query.get_or_404(msg_id)
    tags = [tag.id for tag in found_message.tags]
    form = MessageForm(tags=tags)
    form.set_choices()
    form.message.data = found_message.message
    return render_template('messages/edit.html', form=form, msg=found_message)


@messages_blueprint.route('/new')
@ensure_authenticated
@ensure_correct_user
def new(user_id):
    form = MessageForm(request.form)
    form.set_choices()
    return render_template('messages/new.html', form=form, user_id=user_id)


@messages_blueprint.route('/show/<int:msg_id>', methods=['GET', 'PATCH', 'DELETE'])
@ensure_authenticated
@ensure_correct_user
def show(user_id, msg_id):
    found_message = Message.query.get_or_404(msg_id)
    if request.method == b'PATCH':
        form = MessageForm(request.form)
        form.set_choices()
        if form.validate():
            found_message.message = request.form.get('message')
            found_message.tags = []

            for tag in form.tags.data:
                found_message.tags.append(Tag.query.get(tag))

            db.session.add(found_message)
            db.session.commit()
            return redirect(url_for('messages.index', user_id=user_id))
        else:
            return render_template(url_for('messages/edit.html', form=form, message=found_message))

    if request.method == b'DELETE':
        form = DeleteForm(request.form)
        if form.validate():
            db.session.delete(found_message)
            db.session.commit()
            return redirect(url_for('messages.index', user_id=user_id))
        else:
            return render_template(url_for('messages/edit.html', form=form, message=found_message))

    return render_template('messages/show.html', msg=found_message)

