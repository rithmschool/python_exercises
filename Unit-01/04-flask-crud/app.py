from flask import Flask, render_template, redirect, url_for, request, abort
from snack import Snack
from flask_modus import Modus

app = Flask(__name__)
modus = Modus(app)

# snack1 = Snack(name='GFBrownie', kind='Gluten Free')
# snack2 = Snack(name='Ground Oats', kind='Organic')
# snack3 = Snack(name='Protein Bar', kind='GMO')

# snack_list = [snack1, snack2, snack3]
snack_list = []

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/snacks', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		snack_list.append(Snack(request.form.get('name'), request.form.get('kind')))
		return redirect(url_for('index'))

	return render_template('index.html', snacks=snack_list)

@app.route('/snacks/new')
def new():
    return render_template('new.html')

@app.route('/snacks/<int:id>', methods=['GET', 'POST'])
def show(id):
	try:
		found_snack = [snack for snack in  snack_list if snack.id == id][0]

		if request.method == "POST":
			return redirect(url_for('index'))
		return render_template('show.html', snack=found_snack)
	except IndexError:
		abort(404)

@app.route('/snacks/<int:id>/edit', methods=['GET', 'PATCH', 'DELETE'])
def update(id):
	try:
		found_snack = [snack for snack in snack_list if snack.id == id][0]
		if request.method == b"PATCH":
			found_snack.name = request.form.get('name')
			found_snack.kind = request.form.get('kind')
			return redirect(url_for('index'))

		if request.method == b"DELETE":
			snack_list.remove(found_snack)
			return redirect(url_for('index'))

		return render_template('edit.html', snack=found_snack)
	except IndexError:
		# return redirect("/404.html"), 404, {"Refresh": "1; url=/404.html"}
		abort(404)

@app.errorhandler(404)
def internal_error(error):
	return render_template('404.html')

    
if __name__ == '__main__':
    app.run(debug=True,port=3000)