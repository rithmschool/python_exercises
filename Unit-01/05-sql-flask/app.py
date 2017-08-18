from flask import Flask, render_template, redirect, url_for, request, abort
from flask_modus import Modus
import db

app = Flask(__name__)
modus = Modus(app)

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/snacks', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		db.create_snack(request.form.get('name'), request.form.get('kind'))
		return redirect(url_for('index'))
		
	return render_template('index.html', snacks=db.find_all_snacks())

@app.route('/snacks/new')
def new():
    return render_template('new.html')

@app.route('/snacks/<int:id>', methods=['GET', 'POST'])
def show(id):
	found_snack = db.find_snack(id)

	if found_snack is None:
		abort(404)

	if request.method == "POST":
		return redirect(url_for('index'))

	return render_template('show.html', snack=found_snack)

@app.route('/snacks/<int:id>/edit', methods=['GET', 'PATCH', 'DELETE'])
def update(id):
	found_snack = db.find_snack(id)

	if found_snack is None:
		abort(404)

	if request.method == b"PATCH":
		db.edit_snack(request.form.get('name'), request.form.get('kind'), id)
		return redirect(url_for('index'))

	if request.method == b"DELETE":
		db.remove_snack(id)
		return redirect(url_for('index'))

	return render_template('edit.html', snack=found_snack)

@app.errorhandler(404)
def internal_error(error):
	return render_template('404.html')

    
if __name__ == '__main__':
    app.run(debug=True,port=3000)