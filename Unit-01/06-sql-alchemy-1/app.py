from flask import Flask, render_template, url_for, request, redirect, abort
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
modus = Modus(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/flask-sqlalchemy-snacks'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Snack(db.Model):
   __tablename__ = "snacks"

   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.Text)
   kind = db.Column(db.Text)
   calories = db.Column(db.Integer)

   def __init__(self, name, kind, calories):
   	self.name = name
   	self.kind = kind
   	self.calories = calories

   def __repr__(self):
   	return "This snack is {}. It is a kind of {}. It has {} calories.".format(self.name, self.kind, self.calories)


@app.route('/')
def root():
	return redirect(url_for('index'))

@app.route('/snacks', methods=["GET", "POST"])
def index():
	if request.method == "POST":
		snacks = Snack(request.form['name'], request.form['kind'], request.form['calories'])
		db.session.add(snacks)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('index.html', snacks=Snack.query.all())

@app.route('/snacks/new')
def new():
	return render_template('new.html')

@app.route('/snacks/<int:id>', methods=["GET","PATCH","DELETE"])
def show(id):
	snack = Snack.query.get(id)
	if snack is None:
		abort(404)
	if request.method == b'PATCH':
		snack.name = request.form['name']
		snack.kind = request.form['kind']
		snack.calories = request.form['calories']
		db.session.add(snack)
		db.session.commit()
		return redirect(url_for('index'))
	if request.method == b'DELETE':
		db.session.delete(snack)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('show.html', snack=snack)

@app.route('/snacks/<int:id>/edit')
def edit(id):
	snack = Snack.query.get(id)
	return render_template('edit.html', snack=snack)

if __name__ == '__main__':
	app.run(debug=True, port=3000)