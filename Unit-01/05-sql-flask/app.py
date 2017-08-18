from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
import db

app = Flask(__name__)
modus = Modus(app)


@app.route('/')
def root():
    return redirect(url_for('index'))


@app.route('/snacks', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        kind = request.form.get('kind')
        db.create_snack(name, kind)

        return redirect(url_for('index'))

    return render_template('index.html', snacks=db.find_all_snacks())


@app.route('/snacks/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):
    if id in [snack[0] for snack in db.find_all_snacks()]:
        found_snack = db.find_snack(id)
        if request.method == b'PATCH':
            db.edit_snack(request.form.get('name'), request.form.get('kind'), id)
            return redirect(url_for('index'))

        if request.method == b'DELETE':
            db.remove_snack(id)

            return redirect(url_for('index'))

        return render_template('show.html', snack=found_snack)
    else:
        return render_template('404.html')



@app.route('/snacks/<int:id>/edit')
def edit(id):
    if id in [snack[0] for snack in db.find_all_snacks()]:
        found_snack = db.find_snack(id)
        return render_template('edit.html', snack=found_snack)
    else:
        return render_template('404.html')
        

@app.route('/snacks/new')
def new():
    return render_template('new.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(port=3000, debug=True)
