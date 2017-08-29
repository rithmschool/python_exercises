from flask import Flask, redirect, request, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/more-snacks'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
modus = Modus(app)

class Snack(db.Model):

    __tablename__ = "more-snacks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    kind = db.Column(db.Text)
    tasty = db.Column(db.Boolean)

    def __init__(self, name, kind, tasty):
        self.name = name
        self.kind = kind
        self.tasty = tasty

    def __repr__(self):
        return "{} is a {} type of snack".format(self.name, self.kind)

@app.route('/')
def root():
    return redirect('index')

@app.route('/snacks', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        db.session.add(Snack(request.form.get('name'), request.form.get('kind'), request.form.get('tasty')))
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', snacks=Snack.query.all())
@app.route('/snacks/new')
def new():
    return render_template('new.html')

@app.route('/snacks/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
    snack_picked = Snack.query.get(id)
    if not snack_picked:
        return render_template('404.html')
    if request.method == b"PATCH":
        snack_picked.name = request.form.get('name')
        snack_picked.kind = request.form.get('kind')
        snack_picked.tasty = request.form.get('tasty')
        db.session.add(snack_picked)
        db.session.commit()
        return redirect(url_for('index'))
    if request.method == b"DELETE":
        db.session.delete(snack_picked)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('show.html', snack=snack_picked)

@app.route('/snacks/<int:id>/edit')
def edit(id):
    snack_picked = Snack.query.get(id)
    if not snack_picked:
        return render_template('404.html')
    return render_template('edit.html', snack=snack_picked)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
