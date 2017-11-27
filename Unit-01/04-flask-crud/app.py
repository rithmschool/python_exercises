from flask import Flask, render_template, request, redirect, url_for, abort
from snack import Snack
from functions import find_snack
from flask_modus import Modus

app = Flask(__name__)
modus = Modus(app)

snacks = [Snack('kit-kat', 'unhealthy')]

@app.route("/")
def root():
	return redirect(url_for('index'))

#To read snacks (GET /snacks)
#To create snack (POST /snacks)
@app.route("/snacks", methods=["GET", "POST"])
def index():
	if(request.method == "POST"):
		snacks.append(Snack(request.form.get("name"), request.form.get("kind")))
		return redirect(url_for('index'))
	return render_template("index.html", snacks=snacks)

#To read form to create snack(GET /snacks/new)
@app.route("/snacks/new")
def new():
	return render_template("new.html")

#To read snack (GET /snacks/<int:id>)
#To edit snack (PUT /snacks/<int:id>)
#To delete snack (DELETE /snacks/<int:id>)
@app.route("/snacks/<int:id>", methods=["GET", "PATCH", "DELETE"])
def show(id):
	found = find_snack(id, snacks)
	if found == None:
		abort(404)
		#return redirect(url_for('not_found'))
	if(request.method == b"PATCH"):
		found.name = request.form.get("name")
		found.kind = request.form.get("kind")
		return redirect(url_for('show', id=found.id))
	if(request.method == b"DELETE"):
		snacks.remove(found)
		return redirect(url_for('index'))
	return render_template("show.html", snack = found)

#To read form to edit/delete snack (GET /snacks/<int:id>/edit)
@app.route("/snacks/<int:id>/edit")
def edit(id):
	found = find_snack(id, snacks)
	if found == None:
		abort(404)
	return render_template("edit.html", snack = found)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
	app.run(debug=True)