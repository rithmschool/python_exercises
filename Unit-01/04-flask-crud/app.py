from flask import Flask, redirect, render_template, request, url_for
from flask_modus import Modus
from snack import Snack

app = Flask(__name__)

# This is how we get PATCH requests in
modus = Modus(app)


snack1 = Snack('celery', 'vegetable')

snacks = [snack1];

@app.route('/')
def root():
    return redirect('/snacks')

@app.route('/snacks', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Create a new snack and redirect to /snacks
        new_snack = Snack(request.form.get('name'),
          request.form.get('kind'))
        snacks.append(new_snack)
        return redirect(url_for('index'))
    return render_template('index.html', snacks=snacks)


@app.route('/snacks/new')
def new():
    return render_template('new.html')

@app.route('/snacks/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
    found_snack = [snack for snack in snacks if snack.id == id][0]

    if request.method == b'PATCH':
        found_snack.name = request.form['name']
        found_snack.kind = request.form['kind']
        return redirect(url_for('index'))

    if request.method == b'DELETE':
        snacks.remove(found_snack)
        return redirect(url_for('index'))

    return render_template('show.html', snack=found_snack)

@app.route('/snacks/<int:id>/edit')
def edit(id):
    # Capture the snack they are looking for. Find by Id
    found_snack = [snack for snack in snacks if snack.id == id][0]
    return render_template('edit.html', snack=found_snack)


if __name__ == '__main__':
    app.run(debug=True)