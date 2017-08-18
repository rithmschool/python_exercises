from flask import Flask, redirect, url_for, render_template, request
from flask_modus import Modus
import db

app = Flask(__name__)
modus = Modus(app)

db.create_table()

@app.route('/')
def root():
  return redirect(url_for('index'))

@app.route('/snacks', methods=['GET', 'POST'])
def index():
  if request.method == "POST":
    db.create_snack(request.form['name'], request.form['kind'])
    return redirect(url_for('index'))
  return render_template('index.html', snacks=db.find_all_snacks())

@app.route('/snacks/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):

  if request.method == b"PATCH":
    db.edit_snack(request.form.get('name'), request.form.get('kind'), id)
    return redirect(url_for('index'))

  if request.method == b"DELETE":
    db.snacks.remove_snack(id)
    return redirect(url_for('index'))

  return render_template('show.html', snacks=db.find_snack(id))

@app.route('/snacks/<int:id>/edit')
def edit(id):
  found_snack = db.find_snack(id)
  return render_template('edit.html', snacks=found_snack)

@app.route('/snacks/new')
def new():
    return render_template('new.html')

if __name__ == '__main__':
  app.run(debug=True, port= 3000)