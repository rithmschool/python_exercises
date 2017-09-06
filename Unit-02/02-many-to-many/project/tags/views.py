from flask import redirect, render_template, request, url_for, Blueprint, abort, flash
from project.messages.models import Message
from project.tags.models import Tag
from project.tags.forms import NewTagForm, EditTagForm
from project import db
from flask_wtf.csrf import validate_csrf
from flask_login import login_required, current_user


tags_blueprint = Blueprint(
	'tags',
	__name__,
	template_folder='templates'
)

@tags_blueprint.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		form = NewTagForm(request.form)
		form.set_choices()
		if form.validate_on_submit():
			tag = Tag(form.name.data)
			for message in form.messages.data:
				tag.messages.append(Message.query.get(message))
			db.session.add(tag)
			db.session.commit()
			flash("You have successfully added a Tag!")
			return redirect(url_for('messages.index', user_id=current_user.id))
		else:
			return render_template('departments/new.html', form=form)
		
	return render_template('tags/index.html', tags=Tag.query.order_by(Tag.name).all())

@tags_blueprint.route('/new')
def new():
	form = NewTagForm()
	form.set_choices()
	return render_template('tags/new.html', form=form)

@tags_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
@login_required
def show(id):
	tag = Tag.query.get_or_404(id)
	form = NewTagForm(request.form)
	if request.method == b'DELETE':
		if validate_csrf(request.form.get('csrf_token')) is None:
			db.session.delete(tag)
			db.session.commit()
			flash("You have successfully deleted Tag {}".format(tag.name))
		return redirect(url_for('tags.index', id=tag.id))

	if request.method == b"PATCH":
		form.set_choices()
		if form.validate():
			tag.name = form.name.data
			tag.messages = []
			for message in form.messages.data:
				tag.messages.append(Message.query.get(message))
			db.session.add(tag)
			db.session.commit()
			flash("You have successfully updated a Tag!")
			return redirect(url_for('tags.index'))
		else:
			return render_template('tags/edit.html', tag=tag,form=form)

	return render_template('tags/show.html', tag=tag)

@tags_blueprint.route('/<int:id>/edit', methods=['GET'])
@login_required
def edit(id):
	found_tag = Tag.query.get(id)

	if found_tag is None:
		abort(404)

	messages = [message.id for message in found_tag.messages]
	form = EditTagForm(messages=messages)
	form.set_choices()
	return render_template('tags/edit.html', tag=found_tag, form=form)