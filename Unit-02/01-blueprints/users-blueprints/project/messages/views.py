from flask import Flask, redirect, render_template, url_for, flash, request, Blueprint
from project.messages.models import Message
from project.users.models import User
from project.messages.forms import MessageForm, DeleteForm
from project import db

messages_blueprint = Blueprint('messages', __name__, template_folder='templates')

@messages_blueprint.route('/', methods=["GET", "POST"])
def index(user_id):
	user = User.query.get(user_id)
	if request.method == "POST":
		form = MessageForm(request.form)
		if form.validate():
			created_msg = Message(form.text.data, user.id)
			db.session.add(created_msg)
			db.session.commit()
			flash("You have successfully added a new message!")
			return redirect(url_for('messages.index', user_id=user.id))
		flash("Please enter valid text.")
		return redirect(url_for('messages.new', user_id=user.id, form=form))
	return render_template('messages/index.html', user=user)

@messages_blueprint.route('/new', methods=['GET', 'POST'])
def new(user_id):
	form = MessageForm(request.form)
	user = User.query.get(user_id)
	return render_template('messages/new.html', user=user, form=form)

@messages_blueprint.route('/<int:message_id>', methods=['GET', 'PATCH', 'DELETE'])
def show(user_id, message_id):
	user = User.query.get(user_id)
	message = Message.query.get(message_id)
	if request.method == b"PATCH":
		form = MessageForm(request.form)
		if form.validate():
			message.text = form.text.data
			db.session.add(message)
			db.session.commit()
			flash("You have successfully edited this message.")
			return redirect(url_for('messages.index', user_id=user.id))
		flash("Please enter proper values.")
		return redirect(url_for('messages.edit', user_id=user.id, message_id=message.id, form=form))
	if request.method == b"DELETE":
		delete_form = DeleteForm(request.form)
		if delete_form.validate():
			db.session.delete(message)
			db.session.commit()
			flash("You've successfully deleted {}'s message.".format(user.username))
			return redirect(url_for('messages.index', user_id=user.id))
		return render_template('messages/edit.html', user=user, message=message, delete_form=delete_form)
	return render_template('messages/show.html', user=user, message=message)

@messages_blueprint.route('/<int:message_id>/edit')
def edit(user_id, message_id):
	user = User.query.get(user_id)
	message = Message.query.get(message_id)
	form = MessageForm(obj=message)
	delete_form = DeleteForm(obj=message)
	return render_template('messages/edit.html', user=user, message=message, form=form, delete_form=delete_form)