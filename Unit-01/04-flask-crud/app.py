from flask import Flask, render_template, request, redirect, url_for
from flask_modus import Modus
from snack import Snack

app = Flask(__name__)
modus = Modus(app)

gold_fish = Snack(name="Gold_fish", kind="Crackers" )
almond = Snack(name="Almond", kind="Nuts")
ritz = Snack(name="Ritz", kind="Crackers")

snack_list = [gold_fish, almond, ritz]

@app.route('/snacks', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        snack_list.append(Snack(request.form['name'].capitalize(), request.form['kind'].capitalize()))
        return redirect(url_for("index"))
    return render_template("index.html", snacks = snack_list)

@app.route("/snacks/new")
def new():
	return render_template("new.html")

@app.route('/snack/<int:id>', methods=["GET", "PATCH"])
def show(id):
    # Refactored using a list comprehension!
    found_snack = [snack for snack in  snack_list if snack.id == id][0]
    # Refactor the code above to use a generator so that we do not need to do [0]!
    return render_template('show.html', snack=found_snack)


@app.route('/snacks/<int:id>/edit')
def edit(id):
    # Refactored using a list comprehension!
    found_snack = [snack for snack in  snack_list if snack.id == id][0]
    # Refactor the code above to use a generator so that we do not need to do [0]!
    return render_template('edit.html', snack=found_snack)


if __name__ == "__main__":
    app.run(port=8000, debug=True)