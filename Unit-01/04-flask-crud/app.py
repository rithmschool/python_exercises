from flask import Flask, request, redirect, url_for, render_template
from flask_modus import Modus
from snack import Snack

snack_list = []

app = Flask(__name__)
modus = Modus(app)

def find_snack(id):
    return next(snack for snack in snack_list if snack.id == id)

@app.route('/')
def root():
    return redirect(url_for('snacks'))

@app.route('/snacks', methods = ["GET", "POST"])
def index():
	if request.method == "POST":
		snack_list.append(Snack(request.form["name"],request.form["kind"]))
		return redirect(url_for('index'))
	return render_template('index.html', snack_list=snack_list)

@app.route('/snacks/new')
def new():
    return render_template('new.html')

@app.route('/snacks/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
	found_snack = find_snack(id)
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
	found_snack = find_snack(id)
	return render_template('edit.html', snack=found_snack)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, port=3000)

























