from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello World!"

@app.route("/welcome")
def welcome():
	return "welcome"

@app.route("/welcome/home")
def home():
	return "welcome home"

@app.route("/welcome/back")
def back():
	return "welcome back"

@app.route("/sum")
def sum():
	my_sum = 5+5
	return str(my_sum)

if __name__ == "__main__":
	app.run(debug=True)