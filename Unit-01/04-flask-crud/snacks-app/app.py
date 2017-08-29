from flask import Flask, render_template, request, redirect, url_for, flash
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
from forms import SignupForm
from flask_wtf.csrf import CsrfProtect







app = Flask(__name__)
modus = Modus(app)
CsrfProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/snacks_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "STRING"
db = SQLAlchemy(app)



################SNACK CLASS

class Snack(db.Model):

    __tablename__ = "snacks" # table name will default to name of the model

    # Create the three columns for our table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    image_url = db.Column(db.Text)
    # define what each instance or row in the DB will have (id is taken care of for you)
    def __init__(self, name, image_url):
        self.name = name
        self.image_url = image_url

    # this is not essential, but a valuable method to overwrite as this is what we will see when we print out an instance in a REPL.
    def __repr__(self):
        return "This {} has a url of {} ".format(self.name, self.image_url)




    ########################ROUTES


@app.route('/welcome')
def welcome():
    return render_template('welcome')

@app.route('/')
def hello():
    return "HELLO WORRRRRRRRLD"

@app.route('/snacks', methods=["GET","POST"])
def index():
    form = SignupForm(request.form)
    if request.method == "POST" and form.validate():
        flash("You have successfully added a snack!")
        db.session.add(Snack(request.form['name'], request.form['image_url']))
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method =="POST" and not form.validate():
        return render_template('new.html', form=form)
    return render_template('index.html', snacks=Snack.query.all())


@app.route('/snacks/new', methods=['GET','POST'])
def new():
    form = SignupForm(request.form)
    return render_template('new.html', form=form)

@app.route('/snacks/<int:id>',methods=["GET","PATCH", "DELETE"])
def show(id):
    if request.method == b"PATCH":
        updated_snack = Snack.query.get(id)
        updated_snack.name = request.form['name']
        db.session.add(updated_snack)
        db.session.commit()
        return redirect(url_for('index'))

    if request.method == b"DELETE":
        snack_to_delete = Snack.query.get(id)
        db.session.delete(snack_to_delete)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('show.html', snack=Snack.query.get(id))

@app.route('/snacks/<int:id>/edit')
def edit(id):

    return render_template('edit.html', snack=Snack.query.get(id))















if __name__ == '__main__':
    app.run(port=3000, debug = True)
    #—never use debug true in production. Use only in development
