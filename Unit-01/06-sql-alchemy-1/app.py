from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/snacks-alchemy-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
modus = Modus(app)

class Snack(db.Model):

	__tablename__ = "snacks"  #table name will default to name of the model

	# Create the necessary columns for the table
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	kind = db.Column(db.Text)

	# Define whaat each instance or row in the DB will have (id is taken care of for you)
	def __init__(self, name, kind):
		self.name = name
		self.kind = kind

	# This is not essential, but a valuable method to overwrite as this is what we will se when 
	# we print out an instance in a REPL.
	def __repr__(self):
		return "For this database row, snack: {}, is of kind: {}".format(self.name, self.kind)

# ---------------------------------------------------------------------------

@app.route('/snacks', methods=["GET", "POST"])
def index():
	if request.method == "POST":
	# Using the code below is huge for seeing behind the scenes
		# import IPython; IPython.embed()
		snack = Snack(request.form.get('name'), request.form.get('kind'))
		db.session.add(snack)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('index.html', snack_list=Snack.query.all())

@app.route('/snacks/new')
def new():
	return render_template('new.html')

@app.route('/snacks/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
	found_snack = Snack.query.get(id)

	if request.method == b"PATCH":
		found_snack.name = request.form.get('name')
		found_snack.kind = request.form.get('kind')
		db.session.add(found_snack)
		db.session.commit()
		return redirect(url_for('index'))

	if request.method == b"DELETE":
		db.session.delete(found_snack)
		db.session.commit()
		return redirect(url_for('index'))

	return render_template('show.html', snack=found_snack)

@app.route('/snacks/<int:id>/edit')
def edit(id):
	found_snack = Snack.query.get(id)
	return render_template('edit.html', snack=found_snack)



# ---------------------------------------------------------------------------

if __name__ == '__main__':
	app.run(debug=True, port=3000)