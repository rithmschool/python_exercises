from flask import Flask, redirect, request, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/more-snacks'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Snack(db.Model):

    __tablename__ = "more-snacks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    kind = db.Column(db.Text)

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def __repr__(self):
        return "{} is a {} type of snack".format(self.name, self.kind)

db.create_all()

@app.route('/')
def root():
    return redirect('index')

@app.route('/snacks')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
