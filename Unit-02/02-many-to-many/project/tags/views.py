from flask import redirect, request, render_template, Blueprint, url_for
from project.models import Message, Tag
from project.tags.forms import TagForm, DeleteForm
from project import db

# let's create the tags_blueprint to register in our __init__.py
tags_blueprint = Blueprint(
    'tags',
    __name__,
    template_folder='templates'
)


@tags_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = TagForm(request.form)
        form.set_choices()
        if form.validate():
            tag = Tag(form.text.data)
            for message in form.messages.data:
                tag.messages.append(Message.query.get(message))
            db.session.add(tag)
            db.session.commit()
        else:
            return render_template('tags/new.html', form=form)
    
    return render_template('tags/index.html', tags=Tag.query.all())


@tags_blueprint.route('/<int:tag_id>/edit')
def edit(tag_id):
    found_tag = Tag.query.get_or_404(tag_id)
    messages = [message.id for message in found_tag.messages]
    edit_form = TagForm(messages=messages)
    delete_form = DeleteForm(messages=messages)
    edit_form.set_choices()
    edit_form.text.data = found_tag.text
    return render_template('tags/edit.html', tag=found_tag, edit_form=edit_form, delete_form=delete_form)


@tags_blueprint.route('/new')
def new():
    form = TagForm(request.form)
    form.set_choices()
    return render_template('tags/new.html', form=form)


@tags_blueprint.route('/show/<int:tag_id>', methods=['GET', 'PATCH', 'DELETE'])
def show(tag_id):
    found_tag = Tag.query.get_or_404(tag_id)
    if request.method == b'PATCH':
        form = TagForm(request.form)
        form.set_choices()
        if form.validate():
            found_tag.text = form.text.data
            found_tag.messages = []

            for message in form.messages.data:
                found_tag.messages.append(Message.query.get(message))

            db.session.add(found_tag)
            db.session.commit()
            return redirect(url_for('tags.index'))
        else:
            return render_template(url_for('tags/edit.html', form=form))

    if request.method == b'DELETE':
        form = DeleteForm(request.form)
        if form.validate():
            db.session.delete(found_tag)
            db.session.commit()
            return redirect(url_for('tags.index'))
        else:
            return render_template(url_for('tags/edit.html', form=form))

    return render_template('tags/show.html', tag=found_tag)

