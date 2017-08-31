from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
from snack import Snack

app = Flask(__name__)
modus = Modus(app)

snack1 = Snack(name='apple', kind='fruit')
snack2 = Snack(name='walnuts', kind='nut')
snack3 = Snack(name='carrot', kind='vegetable')

snack_list = [snack1, snack2, snack3]

@app.route('/snacks', methods=["GET", "POST"])
def index():
	if request.method == "POST":

	# Using the code below is huge for seeing behind the scenes
		# import IPython; IPython.embed()
	# With code/IPython "breakpoint" above I was able to figure 
	# out how to add a snack to snack_list 

		snackName = request.form['name']
		snackKind = request.form['kind']
		snack_list.append(Snack(name=snackName, kind=snackKind))
		return redirect(url_for('index'))
	return render_template('index.html', snack_list=snack_list)

@app.route('/snacks/new')
def new():
	return render_template('new.html')

@app.route('/snacks/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
	# find a snack based on its id
	found_snack = next(snack for snack in snack_list if snack.id == id) 
	if request.method == b"PATCH":
		found_snack.name = request.form.get('name')
		found_snack.kind = request.form.get('kind')
		return redirect(url_for('index'))

	if request.method == b"DELETE":
		snack_list.remove(found_snack)
		return redirect(url_for('index'))		
    # if we are showing information about a toy
	return render_template('show.html', snack=found_snack)

@app.route('/snacks/<int:id>/edit')
def edit(id):
	found_snack = next(snack for snack in snack_list if snack.id == id)
	return render_template('edit.html', snack=found_snack)

if __name__ == '__main__':
	app.run(debug=True, port=3000)

