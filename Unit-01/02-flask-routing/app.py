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
  if string == 'add':
    return add(num1,num2)
  elif string == 'subtract':
    return subtract(num1,num2)
  elif string == 'multiply':
    return multiply(num1,num2)    	
  elif string == 'divide':
    return divide(num1,num2)    	

if __name__ == '__main__':
  app.run(debug=True, port=3000)
