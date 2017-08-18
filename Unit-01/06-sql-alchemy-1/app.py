from flask import Flask, render_template,url_for,redirect,request
##from classSnack import Snack

from flask_sqlalchemy import SQLAlchemy 

from flask_modus import Modus


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgres://localhost/snacks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

modus = Modus(app)

snacks = db.get_all_snacks()

@app.route('/')
def root():
	pass

@app.route('/snacks', methods=["GET","POST"])
def index():
	if request.method == "POST":
		db.add_snack(request.form['name'],request.form['kind'])
		return redirect(url_for('index'))

	return render_template('index.html', snacks=db.get_all_snacks())


@app.route('/snacks/new')
def new():
	return render_template('new.html')

@app.route('/snacks/<int:id>', methods=["GET","PATCH","DELETE"])
def show(id):
	for snack in snacks:
		if snack.id == id:
			found_snack = snack

	if request.method == b"PATCH":
		found_snack.name = request.form['name']
		found_snack.name = request.form['kind']
		return redirect(url_for('index'))

	if request.method == b"DELETE":
		snacks.remove(found_snack)
		return redirect(url_for('index'))

	return render_template('show.html',snack=found_snack)

@app.route('/snacks/<int:id>/edit')
def edit(id):
	for snack in snacks:
		if snack.id == id:
			found_snack = snack
	return render_template('edit.html',snack=found_snack)


if __name__ == '__main__':
	app.run(debug=True)
