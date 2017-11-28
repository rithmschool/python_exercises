from flask import Flask, render_template, request, url_for, redirect
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
modus = Modus(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/snacks_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class Snacks(db.Model):

	__tablename__ = 'snacks'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	kind = db.Column(db.Text)

	def __init__(self, name, kind):
		self.name = name
		self.kind = kind


snickers = Snacks(name='snickers', kind='candybar')
eggs = Snacks(name='eggs', kind='candy')
snack_list = [snickers, eggs]

#SHOW ALL SNACKS
@app.route('/snacks', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		snack_list.append(Snacks(request.form['snack'], request.form['kind']))
		return redirect(url_for('index'))

	return render_template('index.html', snack_list=snack_list)

#FORM FOR NEW SNACK
@app.route('/snacks/new')
def new():
	return render_template('new.html')

#VIEW BY SNACK
@app.route('/snacks/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):
	for snack in snack_list:
		if snack.id == id:
			found_snack = snack

	if request.method == b'PATCH':
		found_snack.name = request.form['snack']
		found_snack.kind = request.form['kind']
		return redirect(url_for('index'))

	if request.method == b'DELETE':
		snack_list.remove(found_snack)
		return redirect(url_for('index'))

	return render_template('show.html', snack=found_snack)


@app.route('/snacks/<int:id>/edit')
def edit(id):
	for snack in snack_list:
		if snack.id == id:
			found_snack = snack
	return render_template('edit.html', snack=found_snack)
	




if __name__ == '__main__':
	app.run(debug=True)
