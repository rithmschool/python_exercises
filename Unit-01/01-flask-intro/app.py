from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
	return 'welcome'

@app.route('/welcome/home')
def welcome_home():
	return 'welcome home'

@app.route('/welcome/back')
def welcome_back():
	return 'welcome back'

@app.route('/welcome/sum')
def sum():
	sum = 5+5
	return str(sum)


if __name__ == '__main__':
	app.run(debug=True)