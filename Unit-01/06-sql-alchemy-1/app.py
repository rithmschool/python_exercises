from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus

snack_list=[]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/snacks-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
modus = Modus(app)

class Snack(db.Model):
	__tablename__ = "snacks"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	kind = db.Column(db.Text)

	def __init__(self, name, kind):
		self.name = name
		self.kind = kind

	def __repr__(self):
		return f"Name: {self.name}; Kind: {self.kind}" 		

@app.route('/')
@app.route('/snacks', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		new_snack=Snack(
			request.values.get('name'), 
			request.values.get('kind')
			)
		db.session.add(new_snack)
		db.session.commit()

		return redirect(url_for('index'))	
	return render_template('index.html', snacks=Snack.query.all())

@app.route('/snacks/new')
def new():
	return render_template('new.html')

@app.route('/snacks/<int:id>', methods=['GET', 'DELETE', 'PATCH'])
def show(id):

	found_snack = Snack.query.get(id)

	if request.method == b'PATCH':
		found_snack.name = request.form.get('name')
		found_snack.kind = request.form.get('kind')
		db.session.add(found_snack)
		db.session.commit()

	if request.method == b'DELETE': 
		db.session.delete(found_snack)
		db.session.commit()

	if found_snack and request.method == 'GET':	
		return render_template('show.html', snack=found_snack)

	return redirect(url_for('index'))	

@app.route('/snacks/<int:id>/edit')

def edit(id):
	found_snack = Snack.query.get_or_404(id)
	return render_template('edit.html', snack=found_snack)
			
if __name__ == '__main__':
	app.run(debug=True)	

		