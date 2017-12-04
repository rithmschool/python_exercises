from flask import render_template, url_for, redirect, request, flash, Blueprint
from project.messages.forms import MessageForm, DeleteForm
from project.messages.models import Message
from project.users.models import User
from project import db

messages_blueprint= Blueprint(
	'messages',
	__name__,
	template_folder = 'templates/messages'
	)

@messages_blueprint.route('/', methods=['GET', 'POST'])
def index(user_id):
	delete_form=DeleteForm()
	if request.method == 'POST':
		messages_form = MessageForm(request.form)
		if messages_form.validate():
			new_message = Message(messages_form.content.data, user_id)
			db.session.add(new_message)
			db.session.commit()
			return redirect(url_for('messages.index', user_id=user_id))
		else:
			return render_template('new.html', user=User.query.get(user_id), form=messages_form)	
	return render_template('index.html', user=User.query.get(user_id), delete_form=delete_form)

@messages_blueprint.route('/new')
def new(user_id):
	messages_form=MessageForm()
	return render_template('new.html', user=User.query.get(user_id), form=messages_form)

@messages_blueprint.route('/<int:id>', methods = ['GET', 'PATCH', 'DELETE'])
def show(user_id, id):
	message=Message.query.get(id)
	if request.method == b'PATCH':
		messages_form = MessageForm(request.form)
		if messages_form.validate():
			message.content = messages_form.content.data
			db.session.add(message)
			db.session.commit()
			return redirect(url_for('messages.index', user_id=user_id))
		else:
			return render_template('edit.html', form=messages_form, message=message)
	elif request.method == b'DELETE':
		delete_form=DeleteForm()
		if delete_form.validate():
			db.session.delete(message)
			db.session.commit()
			return redirect(url_for('message.index', user_id=user_id))			
	return render_template('show.html', user_id=user_id, message=message)

@messages_blueprint.route('/<int:id>/edit')
def edit(user_id, id):
	message=Message.query.get(id)
	messages_form=MessageForm()
	return render_template('edit.html', form=messages_form, message=message)
