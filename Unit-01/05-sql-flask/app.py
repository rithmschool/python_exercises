from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
from db import find_all_snacks, create_snack, remove_snack, edit_snack, find_snack
import jinja2

app = Flask(__name__)
modus = Modus(app)

app.jinja_env.undefined = jinja2.StrictUndefined
app.jinja_env.auto_reload = True

# snack = None

@app.route('/snacks', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        create_snack(request.form['name'], request.form['kind'])
        return redirect(url_for('index'))
    return render_template('index.html', snacks=find_all_snacks())

@app.route('/snacks/new')
def new():
    return render_template('new.html')

@app.route('/snacks/<int:id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
    if request.method == b"PATCH": # bytes literal here
        edit_snack(request.form['name'], request.form['kind'], id)
        return redirect(url_for('index'))

    if request.method == b"DELETE": # bytes literal here
        remove_snack(id)
        return redirect(url_for('index'))

    return render_template('show.html', snack=find_snack(id))

@app.route('/snacks/<int:id>/edit')
def edit(id):
    return render_template('edit.html', snack=find_snack(id))

if __name__ == '__main__':
    app.run(port=3000)