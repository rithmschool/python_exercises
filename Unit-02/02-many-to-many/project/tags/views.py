from flask import redirect, render_template, request, url_for, Blueprint, flash
from project.tags.models import Tag
from project.messages.models import Message
from project.tags.forms import TagForm, DeleteForm
from project import db

tags_blueprint = Blueprint(
	'tags',
	__name__,
	template_folder = 'templates'
)


@tags_blueprint.route('/', methods = ['GET', 'POST'])
def index():
	if request.method == "POST":
		form = TagForm(request.form)
		form.set_choices()
		if form.validate_on_submit():
			new_tag = Tag(request.form.get('category'))
			for message in form.messages.data:
				new_tag.messages.append(Message.query.get(message))
			db.session.add(new_tag)
			db.session.commit()
			flash('Tag Created!')
			return redirect(url_for('tags.index'))
		else:
			return render_template('tags/new.html', form = form)
	return render_template('tags/index.html', tags = Tag.query.all())

@tags_blueprint.route('/new')
def new():
	tag_form = TagForm()
	tag_form.set_choices()
	return render_template('tags/new.html', form = tag_form)

@tags_blueprint.route('/<int:id>/edit')
def edit(id):
	found_tag = Tag.query.get_or_404(id)
	messages = [message.id for message in found_tag.messages]
	tag_form = TagForm(messages=messages)
	tag_form.set_choices()
	return render_template('tags/edit.html', tag = found_tag, form =tag_form)

@tags_blueprint.route('/<int:id>', methods = ['GET', 'PATCH', 'DELETE'])
def show(id):
	delete_form = DeleteForm()
	tag = Tag.query.get_or_404(id)
	if request.method == b'PATCH':
		form = TagForm(request.form)
		form.set_choices()
		if form.validate():
			tag.category = form.category.data
			tag.messages = []
			for message in form.messages.data:
				tag.messages.append(Message.query.get(message))
			db.session.add(tag)
			db.session.commit()
			flash('Tag Updated!')
			return redirect(url_for('tags.show', id=id))
		else:
			return render_template('tags/edit.html', tag = tag, form =form)
	if request.method == b'DELETE':
		delete_form = DeleteForm(request.form)
		if delete_form.validate():
			db.session.delete(tag)
			db.session.commit()
			flash('Tag Deleted!')
		return redirect(url_for('tags.index'))
	return render_template('tags/show.html', tag = tag, delete_form = delete_form)