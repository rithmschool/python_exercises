from flask import Flask, render_template, url_for, request, redirect
from flask_modus import Modus
from db import find_all_snacks, create_snack, find_snack, edit_snack, remove_snack

app = Flask(__name__)
modus = Modus(app)

@app.route('/')
def root():
	return redirect(url_for('index'))

@app.route('/snacks', methods=["GET", "POST"])
def index():
	if request.method == "POST":
		create_snack(request.form['name'], request.form['kind'])
		return redirect(url_for('index'))
	return render_template('index.html', snacks=find_all_snacks())

@app.route('/snacks/new')
def new():
	return render_template('new.html')

@app.route('/snacks/<int:id>', methods=["GET","PATCH","DELETE"])
def show(id):
	if request.method == b'PATCH':
		edit_snack(request.form['name'], request.form['kind'], id)
		return redirect(url_for('index'))
	if request.method == b'DELETE':
		remove_snack(id)
		return redirect(url_for('index'))
	return render_template('show.html', snack=find_snack(id))

@app.route('/snacks/<int:id>/edit')
def edit(id):
	snack = find_snack(id)
	return render_template('edit.html', snack=snack)

if __name__ == '__main__':
	app.run(debug=True, port=3000)