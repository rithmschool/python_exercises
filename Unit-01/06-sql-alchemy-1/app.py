from flask import Flask, request, redirect, url_for, render_template
from flask_modus import Modus
# from snack import Snack
# import db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/snacks-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
modus = Modus(app)

class Snack(db.Model):
	__tablename__ = "snacks"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	kind = db.Column(db.Text)
	is_good = db.Column(db.Boolean)

	def __init__(self, name, kind, is_good):
		self.name = name
		self.kind = kind
		self.is_good = is_good

	def __repr__(self):
		return "Name: {} / Kind: {} / Is Good? {}".format(self.name, self.kind, self.is_good)


@app.route('/')
def root():
	return redirect(url_for('index'))

@app.route('/snacks')
def index():
	return render_template('index.html', snacks=Snack.query.all())

@app.route('/snacks/<int:id>/edit', methods=["GET", "PATCH", "DELETE"])
def show(id):
	found_snack = Snack.query.get(id)
	if request.method == b"PATCH":
		found_snack.name = request.form["name"]
		found_snack.kind = request.form["type"] 
		db.session.add(found_snack)
		db.session.commit()
		return redirect(url_for('index'))
	if request.method == b"DELETE":
		db.session.delete(found_snack)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('edit.html', found_snack=found_snack)

@app.route('/snacks/add', methods=["GET", "POST"])
def add():
	if request.method == "POST":
		new_snack = Snack(request.form["name"],request.form["type"])
		db.session.add(new_snack)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('new.html')

if __name__ == "__main__":
	app.run(debug=True, port=3000)