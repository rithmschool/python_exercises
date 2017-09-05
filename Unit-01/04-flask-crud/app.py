from flask import Flask, redirect, url_for, render_template, request
from flask_modus import Modus
from snack import Snack

app = Flask(__name__)
modus = Modus(app)

snickers = Snack( name='Snickers', kind='Candy Bar')
twix = Snack( name='Twix', kind='Candy Bar')
cheetos = Snack( name='Cheetos', kind='Chips')

snacks = [snickers, twix, cheetos]

@app.route('/')
def root():
  return redirect(url_for('index'))

@app.route('/snacks', methods=['GET', 'POST'])
def index():
  if request.method == "POST":
    snacks.append(Snack(request.form['name'], request.form['kind']))
    return redirect(url_for('index'))

  return render_template('index.html', snacks=snacks)

@app.route('/snacks/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):
  found_snack = next(snack for snack in snacks if snack.id == id)

  if request.method == b"PATCH":
    found_snack.name = request.form.get('name')
    return redirect(url_for('index'))

  if request.method == b"DELETE":
    snacks.remove(found_snack)
    return redirect(url_for('index'))

  return render_template('show.html', snacks=found_snack)

@app.route('/snacks/<int:id>/edit')
def edit(id):
  found_snack = next(snack for snack in snacks if snack.id == id)
  return render_template('edit.html', snacks=found_snack)

@app.route('/snacks/new')
def new():
    return render_template('new.html')

if __name__ == '__main__':
  app.run(debug=True, port= 3000)