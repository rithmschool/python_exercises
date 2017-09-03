from flask import redirect, render_template, request, url_for,Blueprint, flash
from project.models import Message, Tag, User
from project.tags.forms import TagForm
from project import db

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
    if form.validate_on_submit():
      tag = Tag(form.tag.data)
      for message in form.messages.data:
        tag.messages.append(Message.query.get(message))
      db.session.add(tag)
      db.session.commit()
      return redirect(url_for('tags.index'))
    else:
      return render_template('tags/new.html', form=form)
  return render_template('tags/index.html', tags=Tag.query.all(), users = User.query.all())

@tags_blueprint.route('/new', methods=['POST', 'GET'])
def new():
  form = TagForm()
  form.set_choices()
  return render_template('tags/new.html', form=form)


@tags_blueprint.route('/<int:id>/edit')
def edit(id):
  found_tag = Tag.query.get_or_404(id)
  messages = [message.id for message in found_tag.messages]
  form = TagForm(messages=messages)
  form.set_choices()
  return render_template('tags/edit.html', tag=found_tag, form=form)

@tags_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):
  found_tag = Tag.query.get_or_404(id)
  if request.method == b"DELETE":
    flash("Message Deleted")
    db.session.delete(found_tag)
    db.session.commit()
    return redirect(url_for('tags.index'))
  if request.method == b"PATCH":
    form = TagForm(request.form)
    form.set_choices()
    if form.validate():
      flash("Message Updated")
      found_tag.tag = form.tag.data
      found_tag.messages = []
      for message in form.messages.data:
        found_tag.messages.append(Message.query.get(message))
      db.session.add(found_tag)
      db.session.commit()
      return redirect(url_for('tags.index'))
    else:
      return render_template('tags/edit.html', form=form)


  return render_template('tags/show.html', tag=found_tag)