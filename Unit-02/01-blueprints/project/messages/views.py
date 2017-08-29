from flask import Blueprint, redirect, url_for, render_template, flash, request
from project.messages.models import Message
from project import db
from project.messages.forms import MessageForm

messages_blueprint = Blueprint(
    'messages',
    __name__,
    template_folder='templates'
)

@messages_blueprint.route('/', methods=["GET", "POST"])
def index(user_id):
    if request.method == "POST":
        form = MessageForm(request.form)
        if form.validate():
            new_message = Message(request.form.get('message'))
            db.session.add(new_message)
            db.session.commit()
            return redirect(url_for('messages.index'))
        return render_template('messages/new.html', form=form)
    return render_template('messages/index.html', messages=Message.query.all())

@messages_blueprint.route('/new')
def new():
    form = MessageForm()
    return render_template('messages/new.html', form=form)
