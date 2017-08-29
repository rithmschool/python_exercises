from flask import redirect, render_template, request, url_for, Blueprint, abort, flash
from project.messages.models import Message
from project.users.models import User
from project.messages.forms import MessageForm, EditMessageForm, DeleteMessageForm
from project import db


messages_blueprint = Blueprint(
	'messages',
	__name__,
	template_folder='templates'
)

@messages_blueprint.route('/', methods=['GET', 'POST'])
def index(user_id):
	found_user = User.query.filter_by(id=user_id).first()

	if request.method == "POST":
		form = MessageForm(request.form)
		if form.validate():
			n_message = Message(request.form.get('text'), found_user.id)
			db.session.add(n_message)
			db.session.commit()
			flash("You have successfully added a Message!")
			return redirect(url_for('messages.index', user_id=found_user.id))
		else:
			return render_template('messages/new.html', user_id=found_user.id, form=form)
		
	return render_template('messages/index.html', user=found_user)

@messages_blueprint.route('/new')
def new(user_id):
	form = MessageForm(request.form)
	return render_template('messages/new.html', user_id=user_id, form=form)

@messages_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(user_id, id):
	found_message = Message.query.filter_by(id=id).first()

	if found_message is None:
		abort(404)

	if request.method == b"DELETE":
		d_form = DeleteMessageForm(request.form)
		if d_form.validate():			
			db.session.delete(found_message)
			db.session.commit()
			flash("You have successfully deleted Message.")
			return redirect(url_for('messages.index', user_id=found_message.user_id))
		else:
			# e_form = EditMessageForm(obj=found_message)
			# return render_template('messages/edit.html', message=found_message, e_form=e_form, d_form=d_form)
			return redirect(url_for('messages.show', user_id=found_message.user_id, id=found_message.id))

	if request.method == b"PATCH":
		e_form = EditMessageForm(request.form)
		if e_form.validate():
			found_message.text = request.form.get('text')
			db.session.add(found_message)
			db.session.commit()
			flash("You have successfully updated a Message!")
			return redirect(url_for('messages.index', user_id=found_message.user_id))
		else:
			d_form = DeleteMessageForm(request.form)
			return render_template('messages/edit.html', message=found_message, e_form=e_form, d_form=d_form)

	return render_template('messages/show.html', message=found_message)

@messages_blueprint.route('/<int:id>/edit', methods=['GET'])
def edit(user_id, id):
	found_message = Message.query.filter_by(id=id).first()
	e_form = EditMessageForm(obj=found_message)
	d_form = DeleteMessageForm()

	if found_message is None:
		abort(404)

	return render_template('messages/edit.html', message=found_message, e_form=e_form, d_form=d_form)