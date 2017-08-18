from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
modus = Modus(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/snacks-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

# Classes
class Snack(db.Model):
    __tablename__ = 'snacks'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    kind = db.Column(db.Text)
    is_good = db.Column(db.Boolean)

    def __init__(self, name, kind, is_good = True):
        self.name = name
        self.kind = kind
        self.is_good = is_good

    def __repr__(self):
        return "This is a snack with the name of {}".format(self.name)

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/snacks', methods = ['GET','POST'])
def index():
    db_snack_list = Snack.query.all()
    if request.method == 'POST':
        db_snack = Snack(request.form.get('name'), request.form.get('kind'))
        db.session.add(db_snack)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('index.html', snacks=db_snack_list)

@app.route('/snacks/new')
def new():
    return render_template('new.html')

@app.route('/snacks/<id>', methods = ['GET','PATCH','DELETE'])
def show(id):
    db_snack = Snack.query.get(id)
    if db_snack == None:
        return page_not_found(404)

    if request.method == b'PATCH':
        db_snack.name = request.form.get('name')
        db_snack.kind = request.form.get('kind')
        db.session.add(db_snack)
        db.session.commit()
        return redirect(url_for('index'))

    if request.method == b'DELETE':
        db.session.delete(db_snack)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('show.html', snack = db_snack)

@app.route('/snacks/<id>/edit')
def edit(id):
    db_snack = Snack.query.get(id)
    return render_template('edit.html', snack = db_snack)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, port=3000)