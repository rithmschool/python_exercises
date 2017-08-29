from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
from snack import Snack

app = Flask(__name__)
modus = Modus(app)

# apples = Snack('apples', 'fruit')
# trailmix = Snack('trailmix', 'nuts')
# granola = Snack('granola bar', 'bar')
# almonds = Snack('almonds', 'nuts')
# bananas = Snack('bananas', 'fruit')

# snack_list = [apples, trailmix, granola, almonds, bananas]

snack_list = []

@app.route('/snacks', methods=["GET", "POST"])
def index():
  if request.method == "POST":
    snack_list.append(Snack(request.form['name'], request.form['kind']))
    return redirect(url_for('index'))
  
  return render_template('index.html', snack_list = snack_list)

@app.route('/snacks/new')
def new():
  return render_template('new.html')

@app.route('/snacks/new')
def create():
  return render_template('new.html', snack_list = snack_list)

@app.route('/snacks/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
  for snack in snack_list:
    if snack.id == id:
      selected_snack = snack

  #if updating the snack
  if request.method == b'PATCH':
    selected_snack.name = request.form['name']
    selected_snack.kind = request.form['kind']
    return redirect(url_for('index'))

  #if deleting the snack
  if request.method == b'DELETE':
    snack_list.remove(selected_snack)
    return redirect(url_for('index'))

  #else show info about the snack  
  return render_template('show.html', snack=selected_snack)

@app.route('/snacks/<int:id>/edit')
def edit(id):
  for snack in snack_list:
    if snack.id == id:
      selected_snack = snack
  return render_template('edit.html', snack=selected_snack)

# @app.route('/edit')
# def edit():
#   return render_template('edit.html', snack_list = snack_list)

if __name__ == '__main__':
  app.run(debug=True, port=4000)