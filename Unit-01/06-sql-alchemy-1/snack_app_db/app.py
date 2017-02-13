from flask import Flask, url_for, render_template, redirect, request
from snack import Snack
from flask_modus import Modus

app = Flask(__name__)
modus = Modus(app)


@app.route('/')
def root():
	return redirect(url_for('index'))

@app.route('/snacks', methods = ['GET','POST'])
def index():
	if request.method == 'POST':
		Snack(request.form['name'], request.form['kind'])
		return redirect(url_for('index'))
	elif request.method == b'PATCH':
		pass
		
	else:
		return render_template('index.html', snacks = Snack.snack_list)


@app.route('/snacks/<int:id>/edit', methods=['GET','PATCH', 'DELETE'])
def edit(id):
	if request.method == 'GET':
		snack = Snack.snack_by_id(id)
		return render_template('edit.html', snack=snack)
	if request.method == b'PATCH':
		snack = Snack.snack_by_id(id)
		snack.name = request.form['name']
		snack.kind = request.form['kind']
		return redirect(url_for('index'))
	if request.method == b'DELETE':
		snack_to_delete = Snack.snack_by_id(id)
		Snack.snack_list.remove(snack_to_delete)
		return redirect(url_for('index'))


@app.route('/snacks/new')
def new():
	return render_template('new.html')

@app.route('/snacks/<int:id>')
def snacks_id(id):
	snack = Snack.snack_by_id(id)
	return render_template('snack.html', snack = snack)


if __name__ == '__main__':
	app.run(port=3000,debug=True)

