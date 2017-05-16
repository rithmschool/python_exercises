from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
from snack import Snack

app = Flask(__name__)
modus = Modus(app) # so we can override default form methods

snickers = Snack(name='snickers',kind='chocolate')
skittles = Snack(name='skittles',kind='candy')

snack_list = [snickers, skittles]
# snack_list = []

@app.route('/snacks', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # gather the value of an input with a name attribute of "name" and a kind attribute of "kind"
        snack_list.append(Snack(request.form['name'], request.form['kind']))
        # respond with a redirect to the route which has a function called "index" (in this case that is '/snacks')
        return redirect(url_for('index'))
    # if the method is GET, just return index.html
    return render_template('index.html', snacks=snack_list)

@app.route('/snacks/new')
def new():
    return render_template('new.html')

@app.route('/snacks/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
    # find a snack based on its id
    found_snack = next(snack for snack in snack_list if snack.id == id)

    if request.method == b"PATCH":
        found_snack.name = request.form["name"]
        found_snack.kind = request.form["kind"]
        return redirect(url_for('index'))

    if request.method == b"DELETE":
        snack_list.remove(found_snack)
        return redirect(url_for('index'))

    return render_template('show.html', snack=found_snack)

@app.route('/snacks/<int:id>/edit')
def edit(id):
    # find a snack based on its id
    found_snack = next(snack for snack in snack_list if snack.id == id)
    return render_template('edit.html', snack=found_snack)
    
if __name__ == '__main__':
    app.run(debug=True,port=3000)      