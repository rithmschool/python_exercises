from flask import Flask, render_template, url_for, redirect, request
from flask_modus import Modus 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/snacks-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
modus = Modus(app)
db = SQLAlchemy(app)

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/snacks', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        Snack(request.form['name'], request.form['kind'])
        return redirect(url_for('index'))
    elif request.method == b'PATCH':
        pass
        
    else:
        return render_template('index.html', snacks = Snack.snack_list)

@app.route('/snacks/<int:id>/edit', methods=['GET','PATCH', 'DELETE'])
def edit(id):
    if request.method == 'GET':
        snack = Snack.snack_by_id(id)
        return render_template('edit.html', snack=snack)
    if request.method == b'PATCH':
        snack = Snack.snack_by_id(id)
        snack.name = request.form['name']
        snack.kind = request.form['kind']
        return redirect(url_for('index'))
    if request.method == b'DELETE':
        snack_to_delete = Snack.snack_by_id(id)
        Snack.snack_list.remove(snack_to_delete)
        return redirect(url_for('index'))

@app.route('/snacks/new')
def new():
    return render_template('new.html')

@app.route('/snacks/<int:id>')
def snacks_id(id):
    snack = Snack.snack_by_id(id)
    return render_template('snack.html', snack = snack)



class Snack(db.Model):
    # DDL, this is what creates the Snack-mapped TABLE
    __tablename__ = "snacks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    type = db.Column(db.Text)
    rating = db.Column(db.Integer)
    # DML, this has NOTHING to do with what the table looks like
    def __init__(self, name, type, rating):
        self.name = name
        self.type = type
        self.rating = rating

    def __repr__(self):
        return "Snack: {}, Type of Snack: {}".format(self.name, self.type)

db.create_all()
# s = Snack('Cheesecake','Artery-Clogging-Decadence', 5)
# db.session.add(s)
# db.session.add(Snack('Oranges', 'Not Apples', 3))
# db.session.add(Snack('Carrots','Rabbit Food', 1))
# db.session.add(Snack('Oreo','Heavenly Cookie', 4))
# db.session.add(Snack('Snickers','Rat Poison', 0))
# db.session.commit()


if __name__ == "__main__":
    app.run(port=3000, debug=True)

