# from the flask library import a class named Flask
from flask import Flask

# create an instance of the Flask class
app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    return "welcome back"

@app.route('/sum')
def sum():
    num = 5 + 5
    return str(num)

if __name__ == "__main__":
    app.run(debug=True, port=3000)