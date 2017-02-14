from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
from project.messages.forms import AddMessageForm, EditMessageForm
from project.messages.models import Message
from project import db
from project.users.models import User


messages_blueprint = Blueprint(
    'messages',
    __name__,
    template_folder = "templates"
)


@messages_blueprint.route('/new', methods=['GET', 'POST'])
def new(user_id):
    this_user = User.query.get(user_id)
    message_form = AddMessageForm(request.form)
    return render_template('/messages/new_message.html', form=message_form, user=this_user)

@messages_blueprint.route('/', methods=['GET', 'POST'])
def index(user_id):
    this_user = User.query.get(user_id)
    add_message_form = AddMessageForm(request.form)
    if request.method == "POST" and add_message_form.validate():
        flash("You have successfully added a message!")
        db.session.add(Message(request.form['message'], user_id))
        db.session.commit()
        return render_template('/messages/user_messages.html', messages=this_user.messages.all(), user=this_user)

    return render_template('/messages/user_messages.html', messages=this_user.messages.all(), user=this_user)



@messages_blueprint.route('/<int:message_id>', methods=['GET', 'POST'])
def edit(user_id, message_id):
    edit_form = EditMessageForm(request.form)
    this_user = User.query.get(user_id)
    return render_template('/messages/edit_message.html', message=Message.query.get(message_id), user=this_user, form=edit_form)



@messages_blueprint.route('/<int:message_id>/updated_messages', methods=['GET', 'POST', 'PATCH'])
def update(user_id, message_id):
    this_user = User.query.get(user_id)
    edit_message_form = EditMessageForm(request.form)
    message_to_update = Message.query.get(message_id)
    if request.method == b"PATCH" and edit_message_form.validate():
            flash("You have successfully edited a message!")
            message_to_update.message = request.form['message']
            db.session.add(message_to_update)
            db.session.commit()
            return render_template('/messages/user_messages.html', messages=this_user.messages.all(), user=this_user)









