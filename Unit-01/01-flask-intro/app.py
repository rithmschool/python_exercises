from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/') 
def root():
	return	redirect(url_for('index'))

@app.route('/welcome')
def index():
	return render_template('index.html')

@app.route('/welcome/home')
def home():
	return render_template('home.html')

@app.route('/welcome/back')
def back():
	return render_template('back.html')

@app.route('/sum')
def sum():
	sum = 5+5
	return f"{sum}"

if __name__ == '__main__':
	app.run(debug=True, port=4000)

