from flask import Flask, request, redirect, url_for, render_template
from snacks import Snack

app = Flask(__name__)

snacks = []

@app.route('/')
def root():
	return redirect(url_for('index'))

@app.route('/snacks', methods=["GET", "POST"])
def index():
	return render_template('index.html', snacks=snacks)


if __name__== '__main__':
	app.run(debug=True, port=3000) 