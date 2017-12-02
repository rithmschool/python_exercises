from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
from snack import Snack


app = Flask(__name__)
modus = Modus(app)

snickers = Snack(name = "snickers", kind = "candy bar")
cheetos = Snack(name = 'cheetos', kind = 'chips')
skittles = Snack(name = 'skittles', kind = 'candy')
peanuts = Snack(name = 'peanuts', kind = 'nuts')

snack_list = [Snack(snickers, cheetos, skittles, peanuts)]

def find_snack(id):
    return [snack for snack in snack_list if snack.id == id][0]


@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/snacks', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        snack_list.append(Snack(request.form['name'], request.form['kind']))  # name from type in new.html#
        return redirect(url_for('index'))
    return render_template('index.html', snacks=snack_list)

@app.route('/snacks/new')
def new():
    return render_template('new.html')

@app.route('/snacks/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
    found_snack = next(find_snack(id))

    if request.method == b"PATCH":
        found_snack.name = request.form['name']
        return redirect(url_for('index'))

    if request.method == b"DELETE":
        snack_list.remove(found_snack)
        return redirect(url_for('index'))

    return render_template('show.html', snack=found_snack)

@app.route('/snacks/<int:id>/edit')
def edit(id):
    #refactored using a list comprehension
    found_snack = next(find_snack(id))
    return render_template('edit.html', snack=found_snack)




if __name__ == ("__main__"):
    app.run(debug=True, port=5000)
