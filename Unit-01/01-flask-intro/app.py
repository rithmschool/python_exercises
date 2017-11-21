from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "built with amazement from Flask"

@app.route("/welcome")
def greet():
	return "welcome"

@app.route("/welcome/home")
def greet_home():
	return "welcome home"

@app.route("/welcome/back")
def greet_back():
	return "welcome back"

@app.route("/sum")
def return_sum():
	sum = 5+5
	return f"{sum}"				

if __name__ == "__main__":
	app.run(debug=True,port=3000)	