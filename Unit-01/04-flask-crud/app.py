from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
from snack import Snack

app = Flask(__name__)
modus = Modus(app)

jelly_beans = Snack('jelly beans', 'candy')
nuts = Snack('nuts', 'salty')
pretzels = Snack('pretzels', 'salty')
grasshoppers = Snack('grasshoppers', 'insect')

snack_list = [jelly_beans, nuts, pretzels, grasshoppers]

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/snacks', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        snack = Snack(request.form.get('name'), request.form.get('kind'))
        snack_list.append(snack)
        return redirect(url_for('index'))

    return render_template('index.html', snacks=snack_list)

@app.route('/snacks/new')
def new():
    return render_template('new.html')

@app.route('/snacks/<int:id>', methods = ['GET','PATCH','DELETE'])
def show(id):
    snack = [snack for snack in snack_list if snack.id == id][0]
    if request.method == b'PATCH':
        snack.name = request.form.get('name')
        snack.kind = request.form.get('kind')
        return redirect(url_for('index'))

    if request.method == b'DELETE':
        snack_list.remove(snack)
        return redirect(url_for('index'))

    return render_template('show.html', snack = snack)

@app.route('/snacks/<int:id>/edit')
def edit(id):
    snack = [snack for snack in snack_list if snack.id == id][0]
    return render_template('edit.html', snack = snack)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000)