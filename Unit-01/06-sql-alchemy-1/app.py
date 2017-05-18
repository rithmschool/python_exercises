from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
import db

app = Flask(__name__)
modus = Modus(app) # so we can override default form methods

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/sql_alchemy_snacks'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Snack(db.Model):
    __tablename__ = "snacks"

    # Create the three columns for our table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    kind = db.Column(db.Text)

    # define what each instance or row in the DB will have (id is taken care of for you)
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def __repr__(self):
        return "This snack is called {} and is a {} snack".format(self.name, self.kind)

# import IPython; IPython.embed() # run an Ipython debugger

@app.route('/snacks', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # gather the value of an input with a name attribute of "name" and a kind attribute of "kind"
        new_snack = Snack(request.form['name'], request.form['kind'])
        db.session.add(new_snack)
        db.session.commit()
        # respond with a redirect to the route which has a function called "index" (in this case that is '/snacks')
        return redirect(url_for('index'))
    # if the method is GET, just return index.html
    snacks = Snack.query.all()
    return render_template('index.html', snacks=snacks)

@app.route('/snacks/new')
def new():
    return render_template('new.html')

@app.route('/snacks/<int:snack_id>', methods=["GET", "PATCH", "DELETE"])
def show(snack_id):
    # find a snack based on its id
    found_snack = Snack.query.get_or_404(snack_id)

    if request.method == b"PATCH":
        found_snack.name = request.form["name"]
        found_snack.kind = request.form["kind"]
        db.session.add(found_snack)
        db.session.commit()
        return redirect(url_for('index'))

    if request.method == b"DELETE":
        db.session.delete(found_snack)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('show.html', snack=found_snack)

@app.route('/snacks/<int:snack_id>/edit')
def edit(snack_id):
    # find a snack based on its id
    found_snack = Snack.query.get_or_404(snack_id) # NEW!
    return render_template('edit.html', snack=found_snack)
    
if __name__ == '__main__':
    app.run(debug=True,port=3000)      