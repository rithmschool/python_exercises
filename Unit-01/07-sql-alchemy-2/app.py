from flask import Flask, render_template, redirect, url_for, request, abort, flash
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
from forms import AuthorForm, BookForm, Edit_AuthorForm, Edit_BookForm
import os

app = Flask(__name__)
modus = Modus(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/flask_sql_authors'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

class Author(db.Model):
	__tablename__ = "authors"

	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)
	books = db.relationship('Book', backref='author', lazy='dynamic')

	def __init__(self,first_name, last_name):
		self.first_name = first_name;
		self.last_name = last_name;

	def __repr__(self):
		return "Author name is {} {}".format(self.first_name, self.last_name)

class Book(db.Model):
	__tablename__ = "books"

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Text)
	pages = db.Column(db.Integer)
	publisher_name = db.Column(db.Text)
	author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

	def __init__(self,title, pages, publisher_name, author_id):
		self.title = title;
		self.pages = pages;
		self.publisher_name = publisher_name;
		self.author_id = author_id;

	def __repr__(self):
		return "Book name is {} with {} pages.".format(self.title, self.pages)

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/authors', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		form = AuthorForm(request.form)
		if form.validate():
			n_author = Author(request.form.get('first_name'), request.form.get('last_name'))
			db.session.add(n_author)
			db.session.commit()
			flash("You have successfully added an Author!")
			return redirect(url_for('index'))
		else:
			return render_template('authors/new.html', form=form)

	a_list = Author.query.order_by(Author.first_name).all()
		
	return render_template('authors/index.html', authors=a_list)

@app.route('/authors/new')
def new():
	form = AuthorForm(request.form)
	return render_template('authors/new.html', form=form)

@app.route('/authors/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):
	found_author = Author.query.filter_by(id=id).first()

	if found_author is None:
		abort(404)

	if request.method == b"DELETE":
		db.session.delete(found_author)
		db.session.commit()
		flash("You have successfully deleted Author {} {}".
			format(found_author.first_name, found_author.last_name))
		return redirect(url_for('index'))

	if request.method == b"PATCH":
		form = Edit_AuthorForm(request.form)
		if form.validate():
			found_author.first_name = request.form.get('first_name')
			found_author.last_name = request.form.get('last_name')
			db.session.add(found_author)
			db.session.commit()
			flash("You have successfully updated an Author!")
			return redirect(url_for('index'))
		else:
			return render_template('authors/edit.html', author=found_author, form=form)

	return render_template('authors/show.html', author=found_author)

@app.route('/authors/<int:author_id>/books', methods=['GET', 'POST'])
def books_index(author_id):
	found_author = Author.query.filter_by(id=author_id).first()

	if request.method == "POST":
		form = BookForm(request.form)
		if form.validate():
			n_book = Book(request.form.get('title'), request.form.get('pages'),
			 request.form.get('publisher_name'), found_author.id)
			db.session.add(n_book)
			db.session.commit()
			flash("You have successfully added a Book!")
			return redirect(url_for('books_index', author_id=found_author.id))
		else:
			return render_template('books/new.html', author_id=found_author.id, form=form)
		
	return render_template('books/index.html', author=found_author)

@app.route('/authors/<int:author_id>/books/new')
def books_new(author_id):
	form = BookForm(request.form)
	return render_template('books/new.html', author_id=author_id, form=form)

@app.route('/authors/<int:author_id>/books/<int:id>', methods=['GET', 'POST',
 'PATCH', 'DELETE'])
def books_show(author_id, id):
	found_book = Book.query.filter_by(id=id).first()

	if found_book is None:
		abort(404)

	if request.method == b"DELETE":
		db.session.delete(found_book)
		db.session.commit()
		flash("You have successfully deleted Book {}".format(found_book.title))
		return redirect(url_for('books_index', author_id=found_book.author_id))

	if request.method == b"PATCH":
		form = Edit_BookForm(request.form)
		if form.validate():
			found_book.title = request.form.get('title')
			found_book.pages = request.form.get('pages')
			found_book.publisher_name = request.form.get('publisher_name')
			db.session.add(found_book)
			db.session.commit()
			flash("You have successfully updated a Book!")
			return redirect(url_for('books_index', author_id=found_book.author_id))
		else:
			return render_template('books/edit.html', book=found_book, form=form)

	return render_template('books/show.html', book=found_book)

@app.route('/authors/<int:id>/edit', methods=['GET'])
def edit(id):
	found_author = Author.query.filter_by(id=id).first()
	form = Edit_AuthorForm(obj=found_author)

	if found_author is None:
		abort(404)

	return render_template('authors/edit.html', author=found_author, form=form)

@app.route('/authors/<int:author_id>/books/<int:id>/edit', methods=['GET'])
def books_edit(author_id, id):
	found_book = Book.query.filter_by(id=id).first()
	form = Edit_BookForm(obj=found_book)

	if found_book is None:
		abort(404)

	return render_template('books/edit.html', book=found_book, form=form)

if __name__ == '__main__':
    app.run(debug=True,port=3000)