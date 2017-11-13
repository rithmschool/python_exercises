from flask import Blueprint, redirect, render_template, request, url_for
from project.messages.models import Message
from project.messages.forms import MessageForm
from project.users.models import User
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
	if request.method == "POST":
		if form.validate():
			db.session.add(Message(request.form.get('text'), found_user.id))
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
	return render_template('messages/new.html', found_user=found_user, form=form)

@messages_blueprint.route('/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(user_id,id):
	found_user = User.query.get_or_404(user_id)
	found_message = Message.query.get_or_404(id)
	form = MessageForm(request.form)
	if request.method == b"PATCH":
		if form.validate():
			found_message.text = request.form.get('text')
			db.session.add(found_message)
			db.session.commit()
			return redirect(url_for('messages.index', user_id=found_user.id))
		return render_template('messages/edit.html', found_user=found_user, found_message=found_message, form=form)
	if request.method == b"DELETE":
		db.session.delete(found_message)
		db.session.commit()
		return redirect(url_for('messages.index', user_id=found_user.id))
	return render_template('messages/show.html', found_message=found_message, found_user = found_user)

@messages_blueprint.route('/<int:id>/edit')
def edit(user_id,id):
	found_user = User.query.get_or_404(user_id)
	found_message = Message.query.get_or_404(id)
	form = MessageForm(obj=found_message)
	return render_template('messages/edit.html', found_user=found_user, found_message = found_message, form=form)


@messages_blueprint.errorhandler(404)
def page_not_found(e):
	return render_template('404.html')
