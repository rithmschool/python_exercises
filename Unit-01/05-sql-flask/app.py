from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
# from snack import Snack
import db

app = Flask(__name__)
modus = Modus(app)

@app.route('/snacks', methods=["GET", "POST"])
def index():
	if request.method == "POST":
	# Using the code below is huge for seeing behind the scenes
		# import IPython; IPython.embed()
		db.add_snack(request.form['name'], request.form['kind'])
		return redirect(url_for('index'))
	return render_template('index.html', snack_list=db.get_all_snacks())

@app.route('/snacks/new')
def new():
	return render_template('new.html')

@app.route('/snacks/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
	found_snack = db.find_snack(id)
	if request.method == b"PATCH":
		db.edit_snack(request.form.get('name'), request.form.get('kind'), id)
		return redirect(url_for('index'))

	if request.method == b"DELETE":

		db.remove_snack(id)
		return redirect(url_for('index'))		
	return render_template('show.html', snack=found_snack)


@app.route('/snacks/<int:id>/edit')
def edit(id):
	found_snack = db.find_snack(id)
	# import IPython; IPython.embed()

	return render_template('edit.html', snack=found_snack)


if __name__ == '__main__':
	app.run(debug=True, port=3000)

