from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Unit 1, Ex 3, Part 1!"


@app.route('/person/<string>/<int:num>')
def person(string,num):
  return render_template('person.html', string=string, num=num)

@app.route('/calculate')
def calculate():
  return render_template("calc.html")    


@app.route('/math') 
def math():
  num1 = int(request.args.get('num1'))
  num2 = int(request.args.get('num2'))
  calculation = request.args.get('calculation')
  if calculation == 'add':
    return add(num1,num2)
  elif calculation == 'subtract':
    return subtract(num1,num2)
  elif calculation == 'multiply':
    return multiply(num1,num2)      
  elif calculation == 'divide':
    return divide(num1,num2)      

def add(num1,num2):
    return f"{num1 + num2}"

def subtract(num1,num2):
    return f"{num1 - num2}"

def multiply(num1,num2):
    return f"{num1 * num2}"

def divide(num1,num2):
    return f"{num1 / num2}"

if __name__ == '__main__':
  app.run(debug=True, port=3000)