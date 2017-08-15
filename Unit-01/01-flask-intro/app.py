# from the flask library import a class named Flask
from flask import Flask

# create an instance of the Flask class
app = Flask(__name__)

# listen for a route to `/` - this is known as the root route
@app.route('/')
# when this route is reached (through the browser bar or someone clicking a link, run the following function)
@app.route('/')
def hello():
	return "Hello World!"

@app.route('/welcome')
def welcome():
	return "welcome"

@app.route('/welcome/home')
def welcomeHome():
	return "welcome home"

@app.route('/welcome/back')
def welcomeBack():
	return "welcome back"

@app.route('/sum')
def sum():
	sum = 5 + 5
	return str(sum)


if __name__ == "__main__":
	app.run(debug=True,port=3000)
