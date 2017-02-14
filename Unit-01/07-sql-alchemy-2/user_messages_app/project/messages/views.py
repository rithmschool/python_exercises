from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
from project.messages.forms import AddMessageForm
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
    message_form = AddMessageForm(request.form)
    if request.method == "POST" and message_form.validate():
        flash("You have successfully added a user!")
        db.session.add(Message(request.form['message'], user_id))
        db.session.commit()
        return render_template('/messages/user_messages.html', messages=this_user.messages.all(), user=this_user)









