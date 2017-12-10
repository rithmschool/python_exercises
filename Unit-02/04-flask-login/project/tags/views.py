from flask import redirect, render_template, request, url_for, flash, Blueprint
from project.models import Message, Tag
from project.tags.forms import DeleteForm, TagForm
from project import db
from project.decorators import ensure_correct_user
from flask_login import login_required



tags_blueprint = Blueprint(
	'tags',
	__name__,
	template_folder='templates'
)



@tags_blueprint.route('/', methods=["GET", "POST"])
@login_required
def index():
	if request.method == "POST":
		form = TagForm(request.form)
		form.set_choices()
		if form.validate():
			tag = Tag(form.text.data)
			for message in form.messages.data:
				tag.messages.append(Message.query.get(message))
			db.session.add(tag)
			db.session.commit()
			flash('Tag Created!')
		else:
			return redirect(url_for('tags.new.html', form=form))
	return render_template('tags/index.html', tags=Tag.query.all())

@tags_blueprint.route('/new')
@login_required
def new():
	form = TagForm()
	form.set_choices()
	return render_template('tags/new.html', form=form)

@tags_blueprint.route('/<int:id>/edit')
@login_required
@ensure_correct_user
def edit(id):
	tag = Tag.query.get_or_404(id)
	messages = [message.id for message in tag.messages]
	form = TagForm(messages=messages)
	form.set_choices()
	delete_form = DeleteForm()
	return render_template('tags/edit.html', tag=tag, form=form, delete_form=delete_form)

@tags_blueprint.route('/<int:id>', methods=["GET", "PATCH", "DELETE"])
@login_required
def show(id):
	tag = Tag.query.get(id)
	delete_form = DeleteForm()
	if request.method == b"PATCH":
		form = TagForm(request.form)
		form.set_choices()
		if form.validate():
			tag.text = form.text.data
			tag.messages = []
			for message in form.messages.data:
				tag.messages.append(Message.query.get(message))
			db.session.add(tag)
			db.session.commit()
			flash('Tag Updated!')
			return redirect(url_for('tags.index'))
		else:
			return render_template('tags/edit.html', form=form, tag=tag, delete_form=delete_form)
	if request.method == b"DELETE":
		delete_form = DeleteForm(request.form)
		if delete_form.validate():
			db.session.delete(tag)
			db.session.commit()
			flash('Tag Deleted!')
			return redirect(url_for('tags.index'))
	return render_template('tags/show.html', tag=tag, form=delete_form)