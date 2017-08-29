from flask import Flask, redirect, render_template, url_for, flash, request, Blueprint
from project.messages.models import Message

messages_blueprint = Blueprint('messages', __name__, template_folder='templates')

@messages_blueprint.route('/users/<int:user_id>/messages', methods=["GET", "POST"])
def index_messages(user_id):
	user = User.query.get(user_id)
	if request.method == "POST":
		form = AddMessageForm(request.form)
		if form.validate():
			created_msg = Message(form.text.data, user.id)
			db.session.add(created_msg)
			db.session.commit()
			flash("You have successfully added a new message!")
			return redirect(url_for('index_messages', user_id=user.id))
		flash("Please enter valid text.")
		return redirect(url_for('new_message', user_id=user.id, form=form))
	return render_template('messages/index.html', user=user)

@messages_blueprint.route('/users/<int:user_id>/messages/new', methods=['GET', 'POST'])
def new_message(user_id):
	form = AddMessageForm(request.form)
	user = User.query.get(user_id)
	return render_template('messages/new.html', user=user, form=form)

@messages_blueprint.route('/users/<int:user_id>/messages/<int:message_id>', methods=['GET', 'PATCH', 'DELETE'])
def show_message(user_id, message_id):
	user = User.query.get(user_id)
	message = Message.query.get(message_id)
	if request.method == b"PATCH":
		form = AddMessageForm(request.form)
		if form.validate():
			message.text = form.text.data
			db.session.add(message)
			db.session.commit()
			flash("You have successfully edited this message.")
			return redirect(url_for('index_messages', user_id=user.id))
		flash("Please enter proper values.")
		return redirect(url_for('edit_message', user_id=user.id, message_id=message.id, form=form))
	if request.method == b"DELETE":
		db.session.delete(message)
		db.session.commit()
		flash("You've successfully deleted {}'s message.".format(user.username))
		return redirect(url_for('index_messages', user_id=user.id))
	return render_template('messages/show.html', user=user, message=message)

@messages_blueprint.route('/users/<int:user_id>/messages/<int:message_id>/edit')
def edit_message(user_id, message_id):
	user = User.query.get(user_id)
	message = Message.query.get(message_id)
	form = AddMessageForm(obj=message)
	return render_template('messages/edit.html', user=user, message=message, form=form)