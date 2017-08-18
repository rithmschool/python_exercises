from flask import Flask, redirect, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus

app = Flask(__name__)
modus=Modus(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/snacks'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Snacks(db.Model):
	__tablename__ = 'snacks'

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.Text)
	kind = db.Column(db.Text)

	def __init__(self,name,kind):
		self.name = name
		self.kind = kind


@app.route('/')
def root():
	return redirect(url_for('index'))

@app.route('/snacks', methods = ['GET', 'POST'])
def index():
	snack_list = Snacks.query.order_by(Snacks.id).all()
	if request.method == "POST":
		snack_name = request.form.get('name')
		snack_kind = request.form.get('kind')
		new_snack = Snacks(snack_name,snack_kind)
		db.session.add(new_snack)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('index.html', snacks=snack_list)

@app.route('/snacks/new')
def new():
	return render_template('new.html')

@app.route('/snacks/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):
	found_snack = Snacks.query.get(id)
	
	if request.method == b'PATCH':
		found_snack.name = request.form.get('name')
		found_snack.kind = request.form.get('kind')
		db.session.add(found_snack)
		db.session.commit()
		return redirect(url_for('index'))

	if request.method == b'DELETE':
		db.session.delete(found_snack)
		db.session.commit()
		return redirect(url_for('index'))

	return render_template('show.html', found_snack=found_snack)

@app.route('/snacks/<int:id>/edit')
def edit(id):
	found_snack = Snacks.query.filter_by(id=id).first()
	
	return render_template('edit.html', found_snack=found_snack)


if __name__ == "__main__":
	app.run(port=3000, debug=True)