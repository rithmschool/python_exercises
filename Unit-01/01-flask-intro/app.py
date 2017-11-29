# from the flask library import a class named Flask
from flask import Flask

# create an instance of the Flask class
app = Flask(__name__)

# when this route is reached (through the browser bar or someone clicking a link, run the following function)
@app.route('/welcome')
def welcome():
	return "welcome"

@app.route('/welcome/home')
def welcome_home():
    return "welcome home" 

@app.route('/welcome/back')
def welcome_back():
	return 'welcome back'

@app.route('/sum')
def sum():
	return f"{5+5}"


if __name__ == "__main__":
    app.run(port=3000)
