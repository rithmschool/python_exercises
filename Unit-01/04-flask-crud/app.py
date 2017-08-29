from flask import Flask, render_template, request ,redirect, url_for
from snack import Snack
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
modus = Modus(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/aggregates_exercise'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#Make template snacks
#tim_tams = Snack("Tim Tam","Biscuit")
#redskins = Snack("Red Skins", "Lolly")
#jerky = Snack("Beef Jerky","Jerky")

#Make snack list
#snack_list = [tim_tams, redskins, jerky]

class Snack(db.Model):
	__tablename__ = "snacks" #tablename in DB

	#create all columns for our table
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	kind = db.Column(db.Text)
	calories = db.Column(db.Integer)
	price = db.Column(db.Float)

	def __init__(self, name, kind):
		self.name = name
		self.kind = kind

@app.route("/snacks",methods=["GET", "POST"])
def index():
	get_snacks = Snack.query.all()
	if request.method == "POST":
		new_snack = Snack(request.form["name"], request.form["kind"])
		db.session.add(new_snack)
		db.session.commit()
		return redirect(url_for("index"))
	return render_template("index.html",snacks=get_snacks)

@app.route("/snacks/add")
def add():
	return render_template("add.html")

@app.route("/snacks/<int:id>",methods=["GET","PATCH","DELETE"])
def show(id):
	found_snack = Snack.query.filter_by(id=id).first()
	if request.method == b"PATCH":
		found_snack.name = request.form["name"]
		found_snack.kind = request.form["kind"]
		db.session.add(found_snack)
		db.session.commit()
		return redirect(url_for("index"))
	elif request.method == b"DELETE":
		db.session.delete(found_snack)
		db.session.commit()
		return redirect(url_for("index"))
	return render_template("show.html",one_snack=found_snack)

@app.route("/snacks/<int:id>/edit")
def edit(id):
	found_snack = Snack.query.get(id)
	return render_template("edit.html",one_snack=found_snack)

if __name__ == "__main__":
	app.run(debug=True,port=3000)