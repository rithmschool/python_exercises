from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus 

app = Flask(__name__)
app.config['SQALCHEMY_DATABASE_URI'] = "postgres://localhost/computer-db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
modus = Modus(app)
db = SQLAlchemy(app)

class Snack(db.Model):

	__tablename__ = "snacks"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	kind = db.Column(db.Text)

	
	def __init__(self, name, kind):
		self.name = name
		self.kind = kind


@app.route('/')
def root():
	return redirect(url_for('index'))

@app.route('/snacks', methods=["GET", "POST"])
def index():
	if request.method == 'POST':
		new_snack = Snack(request.form['name'], request.form['kind'])
		db.session.add(new_snack)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('index.html', snacks=Snack.query.all())

@app.route('/snacks/new')
def new():
	return render_template('new.html')

@app.route('/snacks/<int:id>', methods= ["GET", "PATCH", "DELETE"])
def show(id):
	found_snack = find_snack(id)
	if found_snack is None:
		return render_template("404.html"), 404
	if request.method == b'PATCH':
		found_snack.name = request.form['name']
		found_snack.kind = request.form['kind']
		return redirect(url_for('index'))
	if request.method == b'DELETE':
		snacks.remove(found_snack)
		return redirect(url_for('index'))
	return render_template('show.html', snack=found_snack)

	@app.route('/snacks/<int:id>/edit')
	def edit(id):
		found_snack = find_snack(id)
		if found_snack is None:
			return render_template("404.html"), 404
		return render_template('edit.html', snack=found_snack)

if __name__== '__main__':
	app.run(debug=True, port=3000) 