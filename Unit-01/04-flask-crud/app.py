from flask import Flask, render_template, url_for, redirect, request
from flask_modus import Modus
from snack import Snack

app=Flask(__name__)
modus=Modus(app)

snack_list = [Snack(name="licorice", kind="candy"), Snack(name="pistachios", kind="nuts"), Snack(name="strawberries", kind="fruit")]



@app.route("/snacks", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		print(request.form)
		name = request.form.get('name')
		kind = request.form.get('kind')
		snack_list.append(Snack(name, kind))
		return redirect(url_for('index'))
	return render_template("index.html", snacks=snack_list)

@app.route("/snacks/new")
def new():
	return render_template("new.html")

@app.route("/snacks/<int:id>", methods=["GET", "PATCH", "DELETE"])
def show(id):
	try:
		individual_snack = next(snack for snack in snack_list if snack.id == id) or None
	
		if request.method == b"PATCH":
			individual_snack_index = next(index for index, val in enumerate(snack_list) if val.id == id)
			snack_list[individual_snack_index] = individual_snack
			snack_list[individual_snack_index].name = (request.form['name'])
			snack_list[individual_snack_index].kind = (request.form['kind'])

	
		elif request.method == b"DELETE":
			snack_list.remove(individual_snack)
			return redirect(url_for('index'))
	
		return render_template('show.html', snack = individual_snack)	
	except:
		return redirect(url_for('not_found', id=id))

@app.route("/snacks/<int:id>/edit")
def edit(id):
	individual_snack = [snack for snack in snack_list if snack.id == id]
	if individual_snack == []:
		return redirect(url_for('not_found', id=id))
	return render_template('edit.html', snack=individual_snack[0])	



@app.route("/snacks/<int:id>/not-found")
def not_found(id):
	return render_template('404.html')

if __name__ == "__main__":
	app.run(debug=True)

