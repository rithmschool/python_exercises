from flask import Flask

app = Flask(__name__)

@app.route("/")
def welome():
	print(" Welcome!")
	return "Hello, welcome to my app!"

@app.route("/welcome/home")
def welcome_home():
	return "Welcome home!"

@app.route("/welcome/back!")
def welcome_back():
	return "Welcome back!"

if __name__ == "__main__":
    app.run(port=8080, debug=True)
