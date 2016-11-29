from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
	return ""

@app.route("/welcome")
def welcome():
	return "Welcome"

@app.route("/welcome/home")
def welcomeHome():
	return "Welcome home"

@app.route("/welcome/back")
def welcomeBack():
	return "Welcome back!"

@app.route("/sum")
def sum():
	sum = 5+5
	return str(sum)

app.run(debug=True)