from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy #step 1: pip install flask_sqlalchemy psycopg2
from flask_modus import Modus



app = Flask(__name__)
#step 2: app.config to cofig to correct database
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://localhost/flask-snack-app"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
modus = Modus(app)
db = SQLAlchemy(app)


#set up our table
class Snack(db.Model):

    __tablename__ = "snacks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    kind = db.Column(db.Text)

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind


# snack_list = [Snack('snickers', 'candy bar'), Snack('cheetos', 'chips'), Snack('skittles', 'candy'), Snack('peanuts', 'nuts')]


@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/snacks', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_snack = Snack(request.form['name'], request.form['kind'])  # name from type in new.html#
        db.session.add(new_snack)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', snacks=Snack.query.all())

@app.route('/snacks/new')
def new():
    return render_template('new.html')

@app.route('/snacks/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
    found_snack = Snack.query.get(id)

    if request.method == b"PATCH":
        found_snack.name = request.form['name']
        found_snack.kind = request.form['kind']
        db.session.add(found_snack)
        db.session.commit()
        return redirect(url_for('index'))

    if request.method == b"DELETE":
        db.session.delete(found_snack)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('show.html', snack=found_snack)

    return render_template('show.html', snack=found_snack)

@app.route('/snacks/<int:id>/edit')
def edit(id):
    #refactored using a list comprehension
    found_snack = Snack.query.get(id)
    return render_template('edit.html', snack=found_snack)

if __name__ == '__main__':
    app.run(debug=True)
