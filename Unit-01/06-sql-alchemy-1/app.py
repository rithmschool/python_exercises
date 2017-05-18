from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
import jinja2

app = Flask(__name__)
modus = Modus(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/flask-sql-snacks'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.jinja_env.undefined = jinja2.StrictUndefined
app.jinja_env.auto_reload = True

class Snack(db.Model):
    __tablename__ = "snacks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    kind = db.Column(db.Text)

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
    
    def __repr__(self):
        return "This snack: {} is kind: {}".format(self.name, self.kind)

# import IPython; IPython.embed()

@app.route('/snacks', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        db.session.add(Snack(request.form['name'], request.form['kind']))
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', snacks=Snack.query.all())

@app.route('/snacks/new')
def new():
    return render_template('new.html')

@app.route('/snacks/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
    if request.method == b"PATCH": # bytes literal here
        update_snack = Snack.query.get(id)
        update_snack.name = request.form['name']
        update_snack.kind = request.form['kind']
        db.session.add(update_snack)
        db.session.commit()
        return redirect(url_for('index'))

    if request.method == b"DELETE": # bytes literal here
        delete_snack = Snack.query.get(id)
        db.session.delete(delete_snack)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('show.html', snack=Snack.query.get(id))

@app.route('/snacks/<int:id>/edit')
def edit(id):
    return render_template('edit.html', snack=Snack.query.get(id))

if __name__ == '__main__':
    app.run(port=3000, debug=True)