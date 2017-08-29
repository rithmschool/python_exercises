from flask import Flask, render_template, request ,redirect, url_for
from snack import Snack
from flask_modus import Modus
import db

app = Flask(__name__)
modus = Modus(app)


#Make template snacks
#tim_tams = Snack("Tim Tam","Biscuit")
#redskins = Snack("Red Skins", "Lolly")
#jerky = Snack("Beef Jerky","Jerky")

#Make snack list
#snack_list = [tim_tams, redskins, jerky]

@app.route("/snacks",methods=["GET", "POST"])
def index():
	if request.method == "POST":
		db.add_snack(request.form["name"],request.form["kind"])
		return redirect(url_for("index"))
	return render_template("index.html",snacks=db.get_all_snacks())

@app.route("/snacks/add")
def add():
	return render_template("add.html")

@app.route("/snacks/<int:id>",methods=["GET","PATCH","DELETE"])
def show(id):
	found_snack = db.find_snack(id)
	if request.method == b"PATCH":
		db.update_snack(request.form["name"], request.form["kind"],found_snack[0])
		return redirect(url_for("index"))
	elif request.method == b"DELETE":
		db.delete_snack(found_snack[0])
		return redirect(url_for("index"))
	return render_template("show.html",one_snack=found_snack)

@app.route("/snacks/<int:id>/edit")
def edit(id):
	found_snack = db.find_snack(id)
	return render_template("edit.html",one_snack=found_snack)

if __name__ == "__main__":
	app.run(debug=True,port=3000)