from flask import Flask, request, redirect, url_for, render_template
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
from flask_testing import TestCase


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://localhost/sql-alchemy-1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

modus = Modus(app)
db = SQLAlchemy(app)

class Snack(db.Model):

	__tablename__ = 'snacks'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	kind = db.Column(db.Text)

	def __init__(self, name, kind):
		self.name = name
		self.kind = kind

	def __repr__(self):
		return f"Name: {self.name}; Kind: {self.kind}"


@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/snacks', methods = ["GET", "POST"])
def index():
	if request.method == "POST":
		new_snack = Snack(request.form["name"],request.form["kind"])
		db.session.add(new_snack)
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
		found_snack.name = request.form['name']
		found_snack.kind = request.form['kind']
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

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors.html', error=error), 404

@app.errorhandler(500)
def page_not_found(error):
    return render_template('errors.html', error=error), 500

if __name__ == '__main__':
    app.run(port=3000)

























