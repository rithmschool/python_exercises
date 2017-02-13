from flask import Flask, render_template, url_for, redirect, request
from flask_modus import Modus 
from flask_sqlalchemy import SQLAlchemy
from forms import NewForm
from flask_wtf.csrf import CsrfProtect
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/snacks-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
# app.config['SECRET_KEY'] = 'RITHM IS AWESOME!'
modus = Modus(app)
db = SQLAlchemy(app)
CsrfProtect(app)

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/snacks', methods = ['GET','POST'])
def index():
    snacks = Snack.query.all()
    form = NewForm(request.form)
    if request.method == 'POST' and form.validate():
        name=request.form['name']
        type=request.form['type']
        rating=request.form['rating']
        db.session.add(Snack(name,type,rating))
        db.session.commit()
        return redirect(url_for('index'))
    # WHY WONT THIS WORK WITH REDIRECT?
    elif request.method == 'POST' and not form.validate(): 
        return render_template('new.html', form=form)
    return render_template('index.html', snacks=snacks)

@app.route('/snacks/<int:id>/edit', methods=['GET','PATCH', 'DELETE'])
def edit(id):
    form = NewForm(request.form)
    if request.method == 'GET':
        snack = Snack.query.filter_by(id=id).first()
        form = NewForm(obj = snack)
        return render_template('edit.html', snack=snack, form=form)
    if request.method == b'PATCH':
        snack = Snack.snack_by_id(id)
        snack.name = request.form['name']
        snack.kind = request.form['kind']
        return redirect(url_for('index'))
    if request.method == b'DELETE':
        snack = Snack.query.filter_by(id=id)
        db.session.delete(snack)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/snacks/new')
def new():
    form = NewForm()
    return render_template('new.html', form=form)

@app.route('/snacks/<int:id>')
def snacks_id(id):
    snack = Snack.query.filter_by(id=id).first()
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
# DONT NEED TO DO THIS WITH MIGRATIONS
db.create_all()
# s = Snack('Cheesecake','Artery-Clogging-Decadence', 5)
# db.session.add(s)
# db.session.add(Snack('Oranges', 'Not Apples', 3))
# db.session.add(Snack('Carrots','Rabbit Food', 1))
# db.session.add(Snack('Oreo','Heavenly Cookie', 4))
# db.session.add(Snack('Snickers','Rat Poison', 0))
# db.session.commit()

# from IPython import embed; embed()
if __name__ == "__main__":
    app.run(port=3000, debug=True)

