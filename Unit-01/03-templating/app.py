from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/person/<name>/<age>")
def person(name, age):
  name = name.title()
  return render_template("index.html", name=name, age=age)

@app.route("/calculate")
def calc():
  return render_template("calc.html")

@app.route('/math')
def print_name():
  num1 = float(request.args.get('num1'))
  num2 = float(request.args.get('num2'))
  calc = request.args.get('calculation')
  total = 0
  if calc == 'add':
     total = num1+num2

  if calc == 'subtract':
    total = num1-num2

  if calc == 'multiply':
    total = num1*num2

  if calc == 'divide':
    if num2 == 0:
      return 'Please do not divide by 0'
    total = num1/num2

  return 'total {}  {} <form'.format(total, calc)

if __name__ == '__main__':
  app.run(debug=True)



