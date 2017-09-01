from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/flask-sqlalchemy-snacks'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


modus = Modus(app)

class Snack(db.Model):
    __tablename__ = 'snacks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    kind = db.Column(db.Text)

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def __repr__(self):
        return '{} is of type: {}'.format(self.name, self.kind)


@app.route('/')
def root():
    return redirect(url_for('index'))


@app.route('/snacks', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        kind = request.form.get('kind')
        db.session.add(Snack(name, kind))
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('index.html', snacks=Snack.query.order_by(Snack.id).all())


@app.route('/snacks/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):
    if id in [snack.id for snack in Snack.query.all()]:
        found_snack = Snack.query.get(id)
        if request.method == b'PATCH':
            found_snack.name = request.form.get('name')
            found_snack.kind = request.form.get('kind')
            db.session.add(found_snack)
            db.session.commit()
            return redirect(url_for('index'))

        if request.method == b'DELETE':
            db.session.delete(found_snack)
            db.session.commit()

            return redirect(url_for('index'))

        return render_template('show.html', snack=found_snack)
    else:
        return render_template('404.html')



@app.route('/snacks/<int:id>/edit')
def edit(id):
    if id in [snack.id for snack in Snack.query.all()]:
        found_snack = Snack.query.get(id)
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
