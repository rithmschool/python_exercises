from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
import db

app = Flask(__name__)
modus = Modus(app)

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/snacks', methods = ['GET','POST'])
def index():
    db_snack_list = db.find_all_snacks()
    if request.method == 'POST':
        db.create_snack(request.form.get('name'), request.form.get('kind'))
        return redirect(url_for('index'))

    return render_template('index.html', snacks=db_snack_list)

@app.route('/snacks/new')
def new():
    return render_template('new.html')

@app.route('/snacks/<id>', methods = ['GET','PATCH','DELETE'])
def show(id):
    db_snack = db.find_snack(id)
    if request.method == b'PATCH':
        db.edit_snack(request.form.get('name'), request.form.get('kind'), id)
        return redirect(url_for('index'))

    if request.method == b'DELETE':
        db.remove_snack(id)
        return redirect(url_for('index'))

    return render_template('show.html', snack = db_snack)

@app.route('/snacks/<id>/edit')
def edit(id):
    db_snack = db.find_snack(id)
    return render_template('edit.html', snack = db_snack)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)