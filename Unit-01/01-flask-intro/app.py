from flask import flask

app = Flask(__name__)

@app.route("/")
def welome():
	print(" Welcome!")
	return "Hello, welcome to my app!"

@app.route("/Welcome home")
def welcome_home():
	return "Welcome home!"

@app.route("Welcome back!")
def Welcome_back():
	return "Welcome back!"

	if __name__ == "__main__":
		app.run(port=8080, 
			debug=True)
