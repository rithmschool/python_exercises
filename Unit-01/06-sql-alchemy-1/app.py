from flask import Flask, render_template,url_for,redirect,request
##from classSnack import Snack
from flask_modus import Modus
import db

app = Flask(__name__)
modus = Modus(app)

@app.route('/')
def root():
	pass

@app.route('/snacks', methods=["GET","POST"])
def index():
	if request.method == "POST":
		db.add_snack(request.form.get('name'),request.form.get('kind'))
		return redirect(url_for('index'))

	return render_template('index.html', snacks=db.get_all_snacks())


@app.route('/snacks/new')
def new():
	return render_template('new.html')

@app.route('/snacks/<int:id>', methods=["GET","PATCH","DELETE"])
def show(id):
	found_snack = db.find_snack(id)

	if request.method == b"PATCH":
		db.edit_snack(request.form.get('name'),request.form.get('kind'),id)
		return redirect(url_for('index'))

	if request.method == b"DELETE":
		db.delete_snack(id)
		return redirect(url_for('index'))

	return render_template('show.html',snack=found_snack)

@app.route('/snacks/<int:id>/edit')
def edit(id):
	found_snack = db.find_snack(id)
	##db.edit_snack(found_snack[1],found_snack[2],found_snack[0])
	return render_template('edit.html',snack=found_snack)


if __name__ == '__main__':
	app.run(debug=True)
