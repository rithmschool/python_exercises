from flask import Flask, request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://localhost/users-messages"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
modus = Modus(app)
db = SQLAlchemy(app)

class User(db.Model):

	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

@app.route('/')
def root():
	return redirect(url_for('index'))

@app.route('/users', methods=["GET", "POST"])
def index():
  if request.method == "POST":
  	new_user = User(request.form['first_name'], request.form['last_name'])
  	db.session.add(new_user)
  	db.session.commit()
  	return redirect(url_for('index.html'))
  return render_template('users/index.html', users=User.query.all())

@app.route('/users/new')
def new():
	return render_template('users/new.html')

@app.route('/users/<int: id>/edit')
def edit(id):
	found_user = User.query.get(id)
	return render_template('users/edit.html', user=found_user)

@app.route('/users/<int: id>', methods=["GET", "PATCH", "DELETE"])
def show(id):
	found_user = User.query.get(id)
	if request.method == b"PATCH":
		found_user.first_name = request.form['first_name']
		found_user.last_name = request.form['last_name']
		db.session.add(found_user)
		db.session.commit()
		return redirect(url_for('index.html'))
	if request.method == b"DELETE":
		db.session.delete(found_user)
		db.session.commit()
		return redirect(url_for('index.html'))
	return render_template('show/edit.html', user=found_user)

if __name__ == '__main__':
	app.run(debug=True, port=3000)



