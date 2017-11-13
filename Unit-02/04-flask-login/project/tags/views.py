from flask import Blueprint, redirect, render_template, request, url_for
from project.models import Tag, Message
from project.tags.forms import TagForm, DeleteForm
from project import db
from flask_login import login_required


tags_blueprint = Blueprint(
	'tags',
	__name__,
	template_folder='templates'
)


@tags_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def index():
	tag = Tag.query.all()
	form = TagForm(request.form)
	form.set_choices()
	if request.method == "POST":
		if form.validate():
			new_tag = Tag(form.text.data)
			for message in form.messages.data:
				new_tag.messages.append(Message.query.get(message))
			db.session.add(new_tag)
			db.session.commit()
			return redirect(url_for('tags.index'))
		else:
			return render_template('tags/new.html', form=form)
	return render_template('tags/index.html', tag=tag)

@tags_blueprint.route('/new')
@login_required
def new():
	form = TagForm(request.form)
	form.set_choices()
	return render_template('tags/new.html', form=form)


@tags_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
@login_required
def show(id):
	found_tag = Tag.query.get_or_404(id)
	# messages = [message.id for message in found_tag.messages]
	form = TagForm(request.form)
	form.set_choices()
	delete_form = DeleteForm()
	if request.method == b'PATCH':
		if form.validate():
			found_tag.text = request.form.get('text')
			found_tag.messages =[]
			for message in form.messages.data:
				found_tag.messages.append(Message.query.get(message))
			db.session.add(found_tag)
			db.session.commit()
			return redirect(url_for('tags.index'))
		else:
			return render_template('tags/edit.html', tag=found_tag, form=form, delete_form=delete_form)
	if request.method == b'DELETE':
		db.session.delete(found_tag)
		db.session.commit()
		return redirect('tags.index')
	return render_template('tags/show.html', tag=found_tag)


@tags_blueprint.route('/<int:id>/edit')
@login_required
def edit(id):
	tag = Tag.query.get_or_404(id)
	messages = [message.id for message in tag.messages]
	form = TagForm(messages=messages)
	form.set_choices()
	delete_form=DeleteForm()
	return render_template('tags/edit.html', tag=tag, form=form, delete_form=delete_form)















