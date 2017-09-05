from flask import Flask, redirect, url_for, render_template, request
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/snacks-sql-alchemy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
modus = Modus(app)

# notice that all models inherit from SQLAlchemy's db.Model
class Snack(db.Model):
  __table_name__ = "snacks"

   # Create the three columns for our table
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text)
  kind = db.Column(db.Text)
  price = db.Column(db.Float)

  # define what each instance or row in the DB will have (id is taken care of for you)
  def __init__(self, name, kind, price):
    self.name = name
    self.kind = kind
    self.price = price

  # this is not essential, but a valuable method to overwrite as this is what we will see when we print out an instance in a REPL.
    def __repr__(self):
        return "{} is a kind of {} ".format(self.name, self.kind, self.price)


@app.route('/')
def root():
  return redirect(url_for('index'))

@app.route('/snacks', methods=['GET', 'POST'])
def index():
  if request.method == "POST":
    found_snack = Snack(request.form['name'], request.form['kind'],request.form['price'])
    db.session.add(found_snack)
    db.session.commit()
    return redirect(url_for('index'))
  return render_template('index.html', snacks=Snack.query.all())

@app.route('/snacks/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):

  found_snack = Snack.query.get(id)

  if not found_snack:
    return render_template('404.html')

  if request.method == b"PATCH":
    found_snack.name = request.form.get('name')
    db.session.add(found_snack)
    db.session.commit()
    return redirect(url_for('index'))

  if request.method == b"DELETE":
    db.session.delete(found_snack)
    db.session.commit()
    return redirect(url_for('index'))

  return render_template('show.html', snacks=found_snack)

@app.route('/snacks/<int:id>/edit')
def edit(id):
  found_snack = Snack.query.get(id)

  if not found_snack:
    return render_template('404.html')

  return render_template('edit.html', snacks=found_snack)

@app.route('/snacks/new')
def new():
    return render_template('new.html')




if __name__ == '__main__':
  app.run(debug=True, port= 3000)