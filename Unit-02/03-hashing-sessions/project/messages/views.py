from flask import Blueprint, url_for, redirect, render_template, request, flash
from project.models import Message, User
from project.forms import MessageForm, DeleteForm
from project import db
from project.decorators import ensure_correct_user_message
from flask_login import login_required

messages_blueprint = Blueprint(
	'messages',
	__name__,
	template_folder='templates'
)	

@messages_blueprint.route("/", methods=["GET", "POST"])
@login_required
@ensure_correct_user_message
def index(user_id):
	if request.method == "POST":
		message = Message(request.form.get("text"), request.form.get("img"), user_id)
		db.session.add(message)
		db.session.commit()
		flash('Message Created')
		return redirect(url_for('messages.index', user_id=user_id))
	user = User.query.get(user_id)
	return render_template('messages/index.html', user=user)

@messages_blueprint.route("/new")
@login_required
def new(user_id):
	form = MessageForm()
	user = User.query.get(user_id)
	return render_template('messages/new.html', user=user, form=form)

@messages_blueprint.route("/<int:id>", methods = ["GET", "PATCH", "DELETE"])
@login_required
def show(user_id, id):
	message = Message.query.get(id)
	if request.method == b"PATCH":
		form = MessageForm(request.form)
		if form.validate():
			message.text = form.text.data
			message.img = form.img.data
			db.session.add(message)
			db.session.commit()
			flash('Message Updated')
			return redirect(url_for('messages.index', user_id=user_id))
		return render_template('messages/edit.html', message=message, form=form)
	if request.method == b"DELETE":
		delete_form = DeleteForm(request.form)
		if delete_form.validate():
			db.session.delete(message)
			db.session.commit()
			flash('Message Deleted')
		return redirect(url_for('messages.index', user_id=user_id))
	delete_form = DeleteForm()
	return render_template('messages/show.html', message=message, delete_form=delete_form)

@messages_blueprint.route("/<int:id>/edit")
@ensure_correct_user_message
@ensure_authenticated
def edit(user_id, id):
	message = Message.query.get(id)
	form = MessageForm(obj=message)
	return render_template('messages/edit.html', message=message, form=form)