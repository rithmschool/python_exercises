from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://localhost/snacks-db"
modus = Modus(app)
db = SQLAlchemy(app)

class Snack(db.Model):

	__tablename__ = "snacks"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	kind = db.Column(db.Text)
	tastiness = db.Column(db.Integer)


	def __init__(self, name, kind, tastiness):
		self.name = name
		self.kind = kind
		self.tastiness = tastiness

	def __repr__(self):
		return f"id:{self.id}, name:{self.name}"

@app.route("/")
def root():
	return redirect(url_for('index'))

# route to read snacks (GET)
# route to create snack (POST)
@app.route("/snacks", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		new_snack = Snack(
			request.form.get('name'),
			request.form.get('kind'))
		db.session.add(new_snack)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('index.html', snacks = Snack.query.all())

#route to read form to create snack (GET)
@app.route("/snacks/new")
def new():
	return render_template('new.html')

#route to read snack(GET)
#route to update snack(PATCH)
#route to delete snack(DELETE)
@app.route("/snacks/<int:id>", methods=["GET", "DELETE", "PATCH"])
def show(id): 
	found = Snack.query.get_or_404(id)
	if request.method == b"DELETE":
		db.session.delete(found)
		db.session.commit()
		return redirect(url_for('index'))
	if request.method == b"PATCH":
		found.name = request.form.get("name")
		found.kind = request.form.get("kind")
		db.session.add(found)
		db.session.commit()
		return redirect(url_for('show', id=found.id))
	return render_template("show.html", snack=found)

#route to read form to update snack(GET)
@app.route("/snacks/<int:id>/edit")
def edit(id):
	return render_template("edit.html", snack=Snack.query.get_or_404(id))

if __name__ == "__main__":
	app.run(debug=True)