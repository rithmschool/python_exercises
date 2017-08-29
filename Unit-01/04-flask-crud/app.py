from flask import Flask, request, redirect, url_for, render_template
from flask_modus import Modus
from snack import Snack
snack_list = []

app = Flask(__name__)
modus = Modus(app)

def find_snack(id):
    return next(snack for snack in snack_list if snack.id == id)

@app.route('/')
def home():
    return redirect(url_for('snacks'))

@app.route('/snacks', methods = ["GET"])
def snacks():
    return render_template('index.html', snack_list=snack_list)

@app.route('/snacks', methods = ["POST"])
def add_snack():
    snack_list.append(Snack(request.form["name"],request.form["kind"]))
    return redirect(url_for('snacks'))

@app.route('/snacks/new')
def new_snack():
    return render_template('new.html')

@app.route('/snacks/<int:id>')
def show_snack(id):
    snack =  find_snack(id)
    return render_template('show.html', snack=snack)

@app.route('/snacks/<int:id>/edit')
def edit_snack(id):
    snack = find_snack(id)
    return render_template('edit.html',snack=snack)

@app.route('/snacks/<int:id>',methods =["PATCH"])
def update_snack(id):
    snack = find_snack(id)
    snack.name = request.form["name"]
    snack.kind = request.form["kind"]
    return redirect(url_for('snacks'))

@app.route('/snacks/<int:id>', methods =["DELETE"])
def delete_snack(id):
    snack =  find_snack(id)
    snack_list.remove(snack)
    return redirect(url_for('snacks'))

if __name__ == '__main__':
    app.run(debug=True, port=4000)
