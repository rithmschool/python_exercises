from flask import redirect, render_template, request, url_for, flash, Blueprint
from project.messages.forms import MessageForm, DeleteForm
from project.models import Message, User
from project import db

messages_blueprint = Blueprint(
    'messages',
    __name__,
    template_folder='templates'
)


# Messages Routes --------------------------------------------------------------------->
@messages_blueprint.route("/", methods=["GET", "POST"])
def index(user_id):
  if request.method == "POST":
    new_message = Message(request.form['content'], user_id)
    db.session.add(new_message)
    db.session.commit()
    flash("Message created!")
    return redirect(url_for('messages.index', user_id=user_id))
  return render_template("messages/index.html", user=User.query.get(user_id))


@messages_blueprint.route("/new", methods=["GET", "POST"])
def new(user_id):
  return render_template("messages/new.html", user=User.query.get(user_id))


@messages_blueprint.route("/<int:id>/edit")
def edit(user_id, id):
  found_message = Message.query.get(id)
  return render_template("messages/edit.html", message=found_message)


@messages_blueprint.route("/<int:id>", methods=["GET", "PATCH", "DELETE"])
def show(user_id, id):
  found_message = Message.query.get(id)
  if request.method == b"PATCH":
    found_message.content = request.form['content']
    db.session.add(found_message)
    db.session.commit()
    flash("Message updated!")
    return redirect(url_for('messages.index', user_id=user_id))
  if request.method == b"DELETE":
    db.session.delete(found_message)
    db.session.commit()
    flash("Message deleted!")
    return redirect(url_for('messages.index', user_id=user_id))
  return render_template("messages/show.html", message=found_message)
