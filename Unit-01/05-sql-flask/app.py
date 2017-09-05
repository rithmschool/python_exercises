from flask import Flask, request, redirect, url_for, render_template
from flask_modus import Modus
from snack import Snack
import db

app = Flask(__name__)
modus = Modus(app)

# oreos = Snack("Oreos", "cookies", 5)
# ritz = Snack("Ritz", "crackers", 2)
# cheetos = Snack("Cheetos", "chips", 5)
# sunchips = Snack("Sunchips", "chips", 3)
# chipsahoy = Snack("Chips Ahoy", "cookies", 3)
# snacks = [oreos, ritz, cheetos, sunchips, chipsahoy]

@app.route('/')
def root():
	return redirect(url_for('index'))

@app.route('/snacks')
def index():
	return render_template('index.html', snacks=db.find_all_snacks())

@app.route('/snacks/<int:id>/edit', methods=["GET", "PATCH", "DELETE"])
def show(id):
	# found_snack = [snack for snack in snacks if snack.id == id][0]
	found_snack = db.find_snack(id)
	if request.method == b"PATCH":
		db.edit_snack(id, request.form["name"], request.form["type"])
		# found_snack.name = request.form["name"]
		# # found_snack.id = request.form["id"]
		# found_snack.type = request.form["type"]
		# found_snack.deliciousness = request.form["deliciousness"]
		return redirect(url_for('index'))
	if request.method == b"DELETE":
		db.remove_snack(id)
		# snacks.remove(found_snack)
		return redirect(url_for('index'))
	return render_template('edit.html', found_snack=found_snack)

@app.route('/snacks/add', methods=["GET", "POST"])
def add():
	if request.method == "POST":
		new_snack = db.create_snack(request.form["name"],request.form["type"])
		# new_snack = Snack(request.form["name"], request.form["type"], request.form["deliciousness"])
		# snacks.append(new_snack)
		return redirect(url_for('index'))
	return render_template('new.html')

if __name__ == "__main__":
	app.run(debug=True, port=3000)