from flask import Blueprint, render_template, redirect, request, url_for, flash
from project.models import User, Message, Tag
from project.messages.forms import MessageForm, DeleteForm
from project import db
from project.decorators import ensure_correct_user
from flask_login import login_required


messages_blueprint = Blueprint(
	'messages',
	__name__,
	template_folder = 'templates'
)



@messages_blueprint.route('/', methods=["GET", "POST"])
@login_required
def index(user_id):
	user = User.query.get(user_id)
	if request.method == "POST":
		form = MessageForm(request.form)
		form.set_choices()
		if form.validate():
			new_message=Message(form.content.data, user.id)
			for tag in form.tags.data:
				new_message.tags.append(Tag.query.get(tag))
			db.session.add(new_message)
			db.session.commit()
			flash('Message Created!')
			return redirect(url_for('messages.index', user_id=user.id))
		return render_template('new.html', user=user, form=form)	
	return render_template('index.html', user=user)

@messages_blueprint.route('/new')
@login_required
def new(user_id):
	form = MessageForm()
	form.set_choices()
	return render_template('new.html', user=User.query.get(user_id), form=form)

@messages_blueprint.route('/<int:id>/edit')
@login_required
@ensure_correct_user
def edit(user_id, id):
	message=Message.query.get(id)
	tags = [tag.id for tag in message.tags]
	form = MessageForm(tags=tags)
	form.set_choices()
	form.content.data = message.content
	return render_template('edit.html', message=message, form=form)

@messages_blueprint.route('/<int:id>', methods=["GET", "PATCH", "DELETE"])
@login_required
@ensure_correct_user
def show(user_id, id):
	message=Message.query.get(id)
	if request.method == b'PATCH':
		form = MessageForm(request.form)
		form.set_choices()
		if form.validate():
			time = db.func.now()
			message.updated_on = time
			message.content = request.form['content']
			message.tags=[]
			for tag in form.tags.data:
				message.tags.append(Tag.query.get(tag))
			db.session.add(message)
			db.session.commit()
			flash('Message Updated!')
			return redirect(url_for('messages.index', user_id=message.user.id))
		return render_template('edit.html', message=message, form=form)
	if request.method == b'DELETE':
		delete_form = DeleteForm(request.form)
		if delete_form.validate():
			db.session.delete(message)
			db.session.commit()
			flash('Message Deleted!')
			return redirect(url_for('messages.index', user_id=user_id))
	return render_template('show.html', message=message)