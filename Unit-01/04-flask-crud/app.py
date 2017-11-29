from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
from snack import Snack


app = Flask(__name__)
modus = Modus(app)

snickers = Snack(name = "snickers", kind = "candy bar")
cheetos = Snack(name = 'cheetos', kind = 'chips')
skittles = Snack(name = 'skittles', kind = 'candy')
peanuts = Snack(name = 'peanuts', kind = 'nuts')

snack_list = [snickers, cheetos, skittles, peanuts]

@app.route('/snacks', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        snack_list.append(Snack(request.form['name'], request.form['kind']))  # name from type in new.html#
        return redirect(url_for('index'))
    return render_template('index.html', snacks=snack_list)

@app.route('/snacks/new')
def new():
    return render_template('new.html')

@app.route('/snacks/<int:id>')
def show(id):
    for snack in snack_list:
        if snack.id == id:
            found_snack = snack
    return render_template('show.html', snack=found_snack)

@app.route('/snacks/<int:id>/edit')
def edit(id):
    #refactored using a list comprehension
    found_snack = [snack for snack in snack_list if snack.id == id][0]
    return render_template('edit.html', snack=found_snack)


if __name__ == ("__main__"):
    app.run(debug=True, port=5000)
