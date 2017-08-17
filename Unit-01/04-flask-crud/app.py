from flask import Flask, redirect, request, url_for, render_template
from flask_modus import Modus
from snack import Snack

app = Flask(__name__)
modus = Modus(app)

snack_list = []

@app.route('/')
def root():
    return redirect('index')

@app.route('/snacks', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        snack_list.append(Snack(request.form.get('name'), request.form.get('kind')))
        return redirect(url_for('index'))
    return render_template('index.html', snacks=snack_list)

@app.route('/snacks/new')
def new():
    return render_template('new.html')

@app.route('/snacks/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
    found_snack = next(snack for snack in snack_list if snack.id == id)
    if request.method == b"PATCH":
        found_snack.name = request.form.get('name')
        found_snack.kind = request.form.get('kind')
        return redirect(url_for('index'))
    if request.method == b"DELETE":
        snack_list.remove(found_snack)
        return redirect(url_for('index'))
    return render_template('show.html', snack=found_snack)

@app.route('/snacks/<int:id>/edit')
def edit(id):
    found_snack = next(snack for snack in snack_list if snack.id == id)
    return render_template('edit.html', snack=found_snack)
if __name__ == '__main__':
    app.run(debug=True)
