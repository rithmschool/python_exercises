from flask import Flask, redirect, render_template, url_for, flash, request, Blueprint
from project.tags.forms import TagForm, DeleteForm
from project.models import User, Message, Tag
from project import db

tags_blueprint = Blueprint('tags', __name__, template_folder='templates')

@tags_blueprint.route('/', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		form = TagForm(request.form)
		form.set_choices()
		if form.validate_on_submit():
			new_tag = Tag(form.text.data)
			for msg in form.messages.data:
				new_tag.messages.append(Message.query.get(msg))
			db.session.add(new_tag)
			db.session.commit()
			return redirect(url_for('tags.index'))
		else:
			return redirect(url_for('tags.new', form=form))
	return render_template('tags/index.html', tags=Tag.query.all())

@tags_blueprint.route('/new')
def new():
	form = TagForm(request.form)
	form.set_choices()
	return render_template('tags/new.html', form=form)

@tags_blueprint.route('/<int:tag_id>', methods=['GET', 'PATCH', 'DELETE'])
def show(tag_id):
	tag = Tag.query.get(tag_id)
	if request.method == b'PATCH':
		form = TagForm(request.form)
		form.set_choices()
		if form.validate():
			tag.text = form.text.data
			tag.messages = []
			for msg in form.messages.data:
				tag.messages.append(Message.query.get(msg))
			db.session.add(tag)
			db.session.commit()
			return redirect(url_for('tags.index'))
		else:
			return render_template('tags/edit.html', form=form)
	if request.method == b'DELETE':
		delete_form = DeleteForm(request.form)
		if delete_form.validate():
			db.session.delete(tag)
			db.session.commit()
			return redirect(url_for('tags.index'))
	return render_template('tags/show.html', tag=tag)

@tags_blueprint.route('/<int:tag_id>/edit')
def edit(tag_id):
	tag = Tag.query.get(tag_id)
	messages = [message.id for message in tag.messages]
	form = TagForm(messages=messages)
	form.set_choices()
	return render_template('tags/edit.html', tag=tag, form=form)
