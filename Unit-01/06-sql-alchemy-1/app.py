from flask import Flask, render_template, redirect, url_for, request, abort
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
modus = Modus(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/flask_sql_snacks_alchemy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Snack(db.Model):
    __tablename__ = "snacks"

    # Create the three columns for our table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    kind = db.Column(db.Text)
    price = db.Column(db.Float)

    # define what each instance or row in the DB will have
    def __init__(self, name, kind, price):
        self.name = name
        self.kind = kind
        self.price = price

    def __repr__(self):
        return "Snack name is {} and kind {} with price {}".format(self.name,
         self.kind, self.price)

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/snacks', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		n_snack = Snack(request.form.get('name'), request.form.get('kind'),
		 request.form.get('price'))
		db.session.add(n_snack)
		db.session.commit()
		return redirect(url_for('index'))

	s_list = Snack.query.order_by(Snack.name).all()
		
	return render_template('index.html', snacks=s_list)

@app.route('/snacks/new')
def new():
    return render_template('new.html')

@app.route('/snacks/<int:id>', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def show(id):
	found_snack = Snack.query.filter_by(id=id).first()

	if found_snack is None:
		abort(404)

	if request.method == b"DELETE":
		db.session.delete(found_snack)
		db.session.commit()
		return redirect(url_for('index'))

	if request.method == b"PATCH":
		found_snack.name = request.form.get('name')
		found_snack.kind = request.form.get('kind')
		found_snack.price = request.form.get('price')
		db.session.add(found_snack)
		db.session.commit()
		return redirect(url_for('index'))

	if request.method == "POST":
		return redirect(url_for('index'))

	return render_template('show.html', snack=found_snack)

@app.route('/snacks/<int:id>/edit', methods=['GET'])
def update(id):
	found_snack = Snack.query.filter_by(id=id).first()

	if found_snack is None:
		abort(404)

	return render_template('edit.html', snack=found_snack)

@app.errorhandler(404)
def internal_error(error):
	return render_template('404.html')

    
if __name__ == '__main__':
    app.run(debug=True,port=3000)