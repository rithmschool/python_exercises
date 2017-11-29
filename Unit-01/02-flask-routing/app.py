from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Magic Calculator!"


@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
    return f"{num1 + num2}"

@app.route('/subtract/<int:num1>/<int:num2>')
def subtract(num1,num2):
    return f"{num1 - num2}"

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1,num2):
    return f"{num1 * num2}"

@app.route('/divide/<int:num1>/<int:num2>')
def divide(num1,num2):
    return f"{num1 / num2}"

@app.route('/math/<string>/<int:num1>/<int:num2>')
def math(string,num1,num2):
    return f"{string, num1 / num2}"    

app.run(debug=True, port=3000)
