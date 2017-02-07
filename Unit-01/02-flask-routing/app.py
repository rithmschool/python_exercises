# from the flask library import a class named Flask
from flask import Flask

# create an instance of the Flask class
app = Flask(__name__)

# listen for a route to `/` - this is known as the root route
@app.route('/')
# when this route is reached (through the browser bar or someone clicking a link, run the following function)
def hello():
    # this `return` is the response from our server. We are responding with the text "Hello World"
    return "Hello World!"

@app.route('/welcome')
def welcome():
    return "Welcome"

@app.route('/welcome/home')
def welcome_home():
    return "Welcome Home"

@app.route('/welcome/back')
def welcome_back():
    return "Welcome Back"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    sum = num1 + num2
    return str(sum)

@app.route('/subtract/<int:num1>/<int:num2>')
def subtract(num1, num2):
    sum = num1 - num2
    return str(sum)


@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1, num2):
    sum = num1 * num2
    return str(sum)

@app.route('/divide/<int:num1>/<int:num2>')
def division(num1, num2):
    sum = num1 / num2
    return str(sum)

@app.route('/math/<name>/<int:num1>/<int:num2>')
def test(name, num1, num2):
    return name(num1, num2)

if __name__ == "__main__":
    app.run(debug=True, port=3000)