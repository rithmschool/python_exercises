from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
from snack import Snack

app = Flask(__name__)
modus = Modus(app)

snack_list = []

@app.route('/snacks', methods=["GET", "POST"])
def index():
	if request.method == "POST":
		snack_list.append(Snack(request.form.get('name'),request.form.get('kind')))
		return redirect(url_for('index'))
	return render_template('index.html', snack_list=snack_list)

@app.route('/snacks/new')
def new():
	return render_template('new.html')

@app.route('/snacks/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
	found_snack = [snack for snack in  snack_list if snack.id == id][0]
	#if updating the snack
	if request.method == b"PATCH":
		found_snack.name = request.form.get('name')
		found_snack.kind = request.form.get('kind')
		return redirect(url_for('index'))

	#if DELETING the snack
	if request.method == b"DELETE":
		snack_list.remove(found_snack)
		return redirect(url_for('index'))
	#if just showing info about the snack
	return render_template('show.html', snack=found_snack)

@app.route('/snacks/<int:id>/edit')
def edit(id):
	found_snack = [snack for snack in  snack_list if snack.id == id][0]
	return render_template('edit.html', snack=found_snack)


if __name__ == '__main__':
	app.run(debug=True,port=3000)      
