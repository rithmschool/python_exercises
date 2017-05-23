from flask import Blueprint, redirect, render_template, request, url_for
from project.histories.models import History
from project.owners.models import Owner
from project.histories.forms import HistoryForm
from project import db

histories_blueprint = Blueprint(
    'histories',
    __name__,
    template_folder='templates'
)

@histories_blueprint.route('/', methods=["GET","POST"])
def index(owner_id):
    found_owner = Owner.query.get_or_404(owner_id)
    if request.method == "POST":
        form = HistoryForm(request.form)
        if form.validate():
            new_history = History(request.form['city_lived_in'], owner_id)
            db.session.add(new_history)
            db.session.commit()
            return redirect(url_for('histories.index', owner_id=owner_id))
        return render_template('histories/new.html', form=form, owner=found_owner)
    return render_template('histories/index.html', histories=History.query.all(), owner=found_owner)

@histories_blueprint.route('/new')
def new(owner_id):
    found_owner = Owner.query.get_or_404(owner_id)
    form = HistoryForm(request.form)
    return render_template('histories/new.html', form=form, owner=found_owner)

@histories_blueprint.route('/<int:history_id>', methods=["GET", "PATCH", "DELETE"])
def show(owner_id, history_id):
    found_history = History.query.get_or_404(history_id)
    found_owner = Owner.query.get_or_404(owner_id)
    if request.method == b"PATCH":
        form = HistoryForm(request.form)
        if form.validate():
            found_history.city_lived_in = request.form['city_lived_in']
            db.session.add(found_history)
            db.session.commit()
            return redirect(url_for('histories.index', owner_id=owner_id))
        return render_template('histories/edit.html', form=form, owner=found_owner, history=found_history)
    if request.method == b"DELETE":
        db.session.delete(found_history)
        db.session.commit()
        return redirect(url_for('histories.index', owner_id=owner_id))
    return render_template('histories/show.html', owner=found_owner, history=found_history)

@histories_blueprint.route('/<int:history_id>/edit')
def edit(owner_id, history_id):
    found_history = History.query.get_or_404(history_id)
    found_owner = Owner.query.get_or_404(owner_id)
    form = HistoryForm(obj=found_history)
    return render_template('histories/edit.html', form=form, owner=found_owner, history=found_history)
