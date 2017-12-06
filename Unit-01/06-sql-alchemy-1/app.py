from flask import Flask, render_template, url_for, redirect, request
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
modus=Modus(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/snacks-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Snack(db.Model):
	__tablename__="snacks"

	id= db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	kind = db.Column(db.Text)
	rating = db.Column(db.Text)

	def __init__(self, name, kind, rating):
		self.name = name
		self.kind = kind
		self.rating = rating

	def __repr__(self):
		return "Name: {self.name}; Kind: {self.kind}; Rating: {self.rating}"	



@app.route("/snacks", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		name = request.form.get('name')
		kind = request.form.get('kind')
		db.session.add(Snack(name, kind))
		db.session.commit()
		return redirect(url_for('index'))
	return render_template("index.html", snacks=Snack.query.order_by(Snack.id).all())

@app.route("/snacks/new")
def new():
	return render_template("new.html")

@app.route("/snacks/<int:id>", methods=["GET", "PATCH", "DELETE"])
def show(id):
	try:
		individual_snack = Snack.query.get(id)
	
		if request.method == b"PATCH":
			individual_snack.name = (request.form['name'])
			individual_snack.kind = (request.form['kind'])
			db.session.add(individual_snack)
			db.session.commit()

		elif request.method == b"DELETE":
			db.session.delete(individual_snack)
			db.session.commit()
			return redirect(url_for('index'))
	
		return render_template('show.html', snack = individual_snack)	
	except:
		return redirect(url_for('not_found', id=id))

@app.route("/snacks/<int:id>/edit")
def edit(id):
	try:
		individual_snack = Snack.query.get(id)
		return render_template('edit.html', snack=individual_snack)	
	except:
		return redirect(url_for('not_found', id=id))



@app.route("/snacks/<int:id>/not-found")
def not_found(id):
	return render_template('404.html')

if __name__ == "__main__":
	app.run(debug=True)

