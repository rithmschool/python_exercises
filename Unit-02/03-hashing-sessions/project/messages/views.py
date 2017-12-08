from flask import redirect, render_template, request, url_for, Blueprint, flash
from project.messages.models import Message
from project.users.models import User
from project.tags.models import Tag
from project.messages.forms import MessageForm, DeleteForm
from project import db
from project.decorators import ensure_authenticated, ensure_correct_user

messages_blueprint = Blueprint(
	'messages',
	__name__,
	template_folder = 'templates'
)

# Messages
@messages_blueprint.route('/', methods = ["GET", "POST"])
@ensure_authenticated
def index(user_id):
	delete_form = DeleteForm()
	if request.method == 'POST':
		form = MessageForm(request.form)
		form.set_choices()
		if form.validate():
			new_message = Message(request.form.get('content'), user_id)
			for tag in form.tags.data:
				new_message.tags.append(Tag.query.get(tag))
			db.session.add(new_message)
			db.session.commit()
			flash("Message Created!")
		else:
			return render_template('messages/new.html', user = User.query.get_or_404(user_id), form = form)
	return render_template('messages/index.html', user=User.query.get_or_404(user_id), delete_form=delete_form)

@messages_blueprint.route('/new')
@ensure_authenticated
@ensure_correct_user
def new(user_id):
	message_form = MessageForm()
	message_form.set_choices()
	# pass in the user here cause need it for the post request
	return render_template('messages/new.html', user = User.query.get_or_404(user_id), form = message_form)

@messages_blueprint.route('/<int:id>/edit')
@ensure_authenticated
@ensure_correct_user
def edit(user_id, id):
	found_message = Message.query.get_or_404(id)
	tags = [tag.id for tag in found_message.tags]
	message_form = MessageForm(tags=tags)
	message_form.set_choices()
	return render_template('messages/edit.html', message = found_message, form=message_form)

@messages_blueprint.route('/<int:id>', methods = ["GET", "PATCH", "DELETE"])
@ensure_authenticated
@ensure_correct_user
def show(user_id, id):
	found_message = Message.query.get_or_404(id)
	if request.method == b'PATCH':
		form = MessageForm(request.form)
		form.set_choices()
		if form.validate():
			found_message.content = request.form.get('content')
			found_message.tags = []
			for tag in form.tags.data:
				found_message.tags.append(Tag.query.get(tag))
			db.session.add(found_message)
			db.session.commit()
			flash("Message Updated!")
			return redirect(url_for('messages.index', user_id = user_id))
		else:
			return render_template('messages/edit.html', message = found_message, form=form)
	if request.method == b'DELETE':
		delete_form = DeleteForm(request.form)
		if delete_form.validate():
			db.session.delete(found_message)
			db.session.commit()
			flash("Message Deleted!")
		return redirect(url_for('messages.index', user_id = user_id))
	return render_template('messages/show.html', message=found_message)
