from flask import Flask, request, redirect, url_for, render_template
from snacks import Snack
from flask_modus import Modus


app = Flask(__name__)
modus = Modus(app)


snacks = []

def find_snack(id):
	return [snack for snack in snacks if snack.id == id][0]

@app.route('/')
def root():
	return redirect(url_for('index'))

@app.route('/snacks', methods=["GET", "POST"])
def index():
	if request.method == 'POST':
		new_snack = Snack(request.form['snack'])
		snacks.append(new_snack)
		return redirect(url_for('index'))	
	return render_template('index.html', snacks=snacks)

@app.route('/snacks/new')
def new():
	return render_template('new.html')

@app.route('/snacks/<int: id>', methods=["GET", "PATCH"])
def show(id):
	found_snack = find_snack(id)
	if request.method == b'PATCH':
		found_snack.name = request.form['snack']
		return redirect(url_for('index'))
	if request.method == b'DELETE':
		snacks.remove(found_snack)
		return redirect(url_for('index'))
	return render_template('show.html', snack=found_snack)

@app.route('/snacks/<int: id>/edit')
def edit(id):
	found_snack = find_snack(id)
	return render_template('edit.html', snack=found_snack)


if __name__== '__main__':
	app.run(debug=True, port=3000) 