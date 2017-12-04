from flask import Blueprint, redirect, render_template, url_for, request, flash
from project.messages.models import Message
from project.users.models import User
from project.messages.forms import MessageForm
from project import db

messages_blueprint = Blueprint(
	'messages', __name__, template_folder = 'templates')

@messages_blueprint.route('/', methods = ['GET', 'POST'])
def index(user_id):
	user = User.query.get(user_id)
	if request.method == "POST":
		form = MessageForm(request.form)
		if form.validate():
			new_message = Message(request.form['text'], user_id)
			db.session.add(new_message)
			db.session.commit()
			flash("message added")
			return redirect(url_for('messages.index', user_id = user_id))
		return render_template('messages/new.html', user=user, form=form)
	return render_template('messages/index.html', user=user)
		
@messages_blueprint.route('/new')
def new(user_id):
	found_user = User.query.get(user_id)
	form = MessageForm()
	return render_template('messages/new.html', user= found_user, form=form)

@messages_blueprint.route('/<int:id>', methods=['PATCH', 'GET', 'DELETE'])
def show(user_id, id):
	found_message = Message.query.get(id)
	if request.method == b'PATCH':
		form=MessageForm(request.form)
		if form.validate():
			found_message.text = request.form['text']
			db.session.add(found_message)
			db.session.commit()
			flash('message updated')
			return redirect(url_for('messages.index', user_id = user_id))
		return render_template('messages/edit.html', message=found_message,form=form)	
	if request.method == b'DELETE':
		db.session.delete(found_message)
		db.session.commit()
		flash('message deleted')
		return redirect(url_for('messages.index', user_id=user_id))
	return render_template('messages/show.html', message = found_message)	

@messages_blueprint.route('/<int:id>/edit')
def edit(user_id, id):
	found_message = Message.query.get(id)
	form=MessageForm(obj=found_message)
	return render_template('messages/edit.html', message=found_message, form=form)

