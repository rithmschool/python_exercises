from flask import Flask, render_template, request, redirect, url_for
from flask_modus import Modus
from snack import Snack

snacks = [
    Snack("apple", 6),
    Snack("banana", 9),
    Snack("cherry", 6)
]

app = Flask(__name__)
modus = Modus(app)

# list comprehension returns list, found_snack = first item in list
def find_snack(snack_id):
  return [snack for snack in snacks if snack.id == snack_id][0]


@app.route("/")
def root():
  return redirect(url_for('index'))


@app.route('/snacks', methods=["GET", "POST"])
def index():  
  if request.method == 'POST':
    new_snack = Snack(
      request.form.get('snack_type'),
      request.form.get('calories')
      )
    snacks.append(new_snack)
    return redirect(url_for('index'))
  return render_template('index.html', snacks=snacks)


@app.route('/snacks/new')
def new():
  return render_template('new.html')

@app.route('/snacks/<int:id>', methods=["GET","PATCH", "DELETE"])
def show(id):
  found_snack = find_snack(id)
# PATCH REQUIRES b for byte string: b'PATCH'
  if request.method == b'PATCH':
    found_snack.snack_type = request.form['snack_type']
    found_snack.calories = request.form['calories']
    return redirect(url_for('index'))
  if request.method == b'DELETE':
    snacks.remove(found_snack)
    return redirect(url_for('index'))
  return render_template('show.html', snack=found_snack)

@app.route('/snacks/<int:id>/edit')
def edit(id):
  found_snack = find_snack(id)
  return render_template('edit.html', snack=found_snack)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
