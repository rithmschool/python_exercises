from flask import Flask, render_template, request, redirect, url_for
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/computers-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


modus = Modus(app)
db = SQLAlchemy(app)

class Snack(db.Model):

    # gold_fish = Snack(name="Gold_fish", kind="Crackers" )
    # almond = Snack(name="Almond", kind="Nuts")
    # ritz = Snack(name="Ritz", kind="Crackers")

    # snack_list = [gold_fish, almond, ritz]

    __tablename__ = "snacks" # table name will default to name of the model
    
    #refers to teh columns!!!
    # Create the three columns for our table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    kind = db.Column(db.Text)

    #refers to the rows!!!
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        
    def __repr__(self):
        #return self.namels
        #return f"Snack #{self.id}; Name: {self.name}; Kind: {self.kind}"
        return "Snack " + self.name


@app.route('/snacks', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        #snack_list.append(Snack(request.form['name'].capitalize(), request.form['kind'].capitalize()))
        #creating snack from the request 
        #creating the obj here, that will populate the rows !!
        new_snack = Snack(
            request.form.get("name"), 
            request.form.get("kind")
            )
        #adding the snack into the db
        db.session.add(new_snack)
        db.session.commit()

        return redirect(url_for("index"))
    return render_template("index.html", snacks = Snack.query.all())

@app.route("/snacks/new")
def new():
	return render_template("new.html", snacks = Snack.query.all())

@app.route('/snacks/<int:id>/edit')
def edit(id):
    # Refactored using a list comprehension!
    #found_snack = [snack for snack in  snack_list if snack.id == id][0]
    found_snack = Snack.query.get_or_404(id)
    return render_template('edit.html', snack=found_snack, snacks = Snack.query.all())    

@app.route('/snacks/<int:id>/delete')
def delete(id):
    # Refactored using a list comprehension!
    #found_snack = [snack for snack in  snack_list if snack.id == id][0]
    found_snack = Snack.query.get_or_404(id)
    return render_template('delete.html', snack=found_snack, snacks = Snack.query.all())      

@app.route('/snacks/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
    # Refactored using a list comprehension!
    # for toy in toys:
    #     if toy.id == id:
    #         found_toy = toy
    #found_snack = [snack for snack in  snack_list if snack.id == id][0]
    found_snack = Snack.query.get_or_404(id)

     # if we are updating a toy...
    if request.method == b"PATCH":
        #found_snack.name = request.form['new_name']
        #if it was a sweetness, will have to convert to int!!!!
        found_snack.name = request.form['new_name']
        found_snack.kind = request.form['kind']

        #once we have the updated name and snack, we add it to the db
        db.session.add(found_snack)
        db.session.commit()
        return redirect(url_for('index'))
    
    if request.method == b"DELETE": 
        #found_snack.name = request.form['name']  
        #snack_list.remove(found_snack) 
        #deleting it from a db
        db.session.delete(found_snack)
        db.session.commit()

        return redirect(url_for('index'))
    # if we are showing information about a toy
    return render_template('show.html', snack=found_snack)



if __name__ == "__main__":
    app.run(port=8000, debug=True)