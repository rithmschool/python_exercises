from flask import Blueprint, render_template, request, url_for, redirect
from project.users.models import User
from project.messages.models import Message
from project.messages.forms import MessageForm
from project import db

messages_blueprint = Blueprint(
	'messages',
	__name__,
	template_folder='templates'
	)

@messages_blueprint.route('/', methods=["GET", "POST"])
def index(user_id):
	all_messages = Message.query.filter_by(user_id=user_id)
	found_user = User.query.get_or_404(user_id)
	if request.method == "POST":
		form = MessageForm(request.form)
		if form.validate():
			new_message = Message(request.form['message'],user_id)
			db.session.add(new_message)
			db.session.commit()
			return redirect(url_for('messages.index', user_id=user_id))
		return render_template('messages/new.html', user=found_user, form=form)
	return render_template('messages/index.html', user=found_user, messages=all_messages)

@messages_blueprint.route('/new')
def new(user_id):
	found_user = User.query.get_or_404(user_id)
	form = MessageForm()
	return render_template('messages/new.html', user=found_user, form=form)

@messages_blueprint.route('/<int:id>/show', methods=["PATCH", "DELETE"])
def show(user_id, id):
	found_user = User.query.get_or_404(user_id)
	found_message = Message.query.get_or_404(id)
	if request.method == b'PATCH':
		form = MessageForm(request.form)
		if form.validate():
			found_message.message = request.form["message"]
			db.session.add(found_message)
			db.session.commit()
			return redirect(url_for('messages.index', user_id=user_id))
		return render_template('messages/edit.html', form=form, user=found_user, message=found_message)
	elif request.method == b'DELETE':
		db.session.delete(found_message)
		db.session.commit()
		return redirect(url_for('messages.index', user_id=user_id))



@messages_blueprint.route('/<int:id>/edit', methods=["GET", "PATCH", "DELETE"])
def edit(user_id, id):
	found_user = User.query.get_or_404(user_id)
	found_message = Message.query.get_or_404(id)
	form = MessageForm(obj=found_message)
	return render_template('messages/edit.html', form=form, user=found_user, message=found_message)