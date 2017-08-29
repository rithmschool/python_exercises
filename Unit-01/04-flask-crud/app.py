from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
from snack import Snack

app = Flask(__name__)

fruit = Snack(name='fruit', kind='sweet')
granola = Snack(name='granola', kind='sweet')
chips = Snack(name='chips', kind='junk')

snack_list = [fruit, granola, chips]


@app.route('/snacks', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		snack_list.append(Snack(request.form['name'], request.form['kind']))
		return redirect(url_for('index'))
	return render_template('index.html', snack_list=snack_list)

@app.route('/new')
def new():
	return render_template('new.html')

@app.route('/snack/<int:id>/edit')
def edit(id):
	found_snack = [snack for snack in snack_list if snack.id == id][0]
	return render_template('edit.html', snack=found_snack)

@app.route('/snacks/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):
	found_snack = [snack for snack in snack_list if snack.id == id][0]
	if request.method == b"PATCH":
		found_snack.name = request.form['name']
		return redirect(url_for('index'))
	if request.method == b"DELETE":
		snack_list.remove(found_snack)
		return redirect(url_for('index'))
	return render_template('show.html', snack=found_snack)




if __name__ == '__main__':
	app.run(debug=True)