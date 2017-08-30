from flask import Blueprint, redirect, render_template, request, url_for
from project.models import Message, User, Tag
from project.messages.forms import MessageForm, DeleteForm
from project import db

messages_blueprint = Blueprint(
	'messages',
	__name__,
	template_folder='templates'
)

@messages_blueprint.route('/', methods=["GET", "POST"])
def index(user_id):
	found_user = User.query.get_or_404(user_id)
	form = MessageForm(request.form)
	form.set_choices()
	if request.method == "POST":
		if form.validate():
			new_message = Message(form.text.data, found_user.id)
			for tag in form.tags.data:
				new_message.tags.append(Tag.query.get(tag))
			db.session.add(new_message)
			db.session.commit()
			return redirect(url_for('messages.index', user_id = user_id))
		else:
			return render_template('messages/new.html', found_user=found_user, form=form)
	message_list = found_user.messages.order_by(Message.id).all()
	return render_template('messages/index.html', found_user=found_user, message_list=message_list)

@messages_blueprint.route('/new')
def new(user_id):
	found_user = User.query.get_or_404(user_id)
	form = MessageForm(request.form)
	form.set_choices()
	return render_template('messages/new.html', found_user=found_user, form=form)

@messages_blueprint.route('/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(user_id,id):
	found_user = User.query.get_or_404(user_id)
	found_message = Message.query.get_or_404(id)
	form = MessageForm(request.form)
	form.set_choices()
	delete_form = DeleteForm()
	if request.method == b"PATCH":
		if form.validate():
			found_message.text = form.text.data
			found_message.tags=[]
			for tag in form.tags.data:
				found_message.tags.append(Tag.query.get(tag))
			db.session.add(found_message)
			db.session.commit()
			return redirect(url_for('messages.index', user_id=found_user.id))
		return render_template('messages/edit.html', found_user=found_user, found_message=found_message, form=form, delete_form=delete_form)
	if request.method == b"DELETE":
		db.session.delete(found_message)
		db.session.commit()
		return redirect(url_for('messages.index', user_id=found_user.id))
	return render_template('messages/show.html', found_message=found_message, found_user = found_user)

@messages_blueprint.route('/<int:id>/edit')
def edit(user_id,id):
	found_user = User.query.get_or_404(user_id)
	found_message = Message.query.get_or_404(id)
	tags = [tag.id for tag in found_message.tags]
	form = MessageForm(tags=tags)
	form.set_choices()
	delete_form=DeleteForm()
	return render_template('messages/edit.html', found_user=found_user, found_message = found_message, form=form, delete_form=delete_form)


@messages_blueprint.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')
