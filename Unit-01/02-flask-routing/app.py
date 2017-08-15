from flask import Flask
app = Flask(__name__)

@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    return str(num1+num2)

@app.route("/subtract/<int:num1>/<int:num2>")
def subtract(num1, num2):
    return str(num1-num2)

@app.route("/divide/<int:num1>/<int:num2>")
def divide(num1, num2):
    return str(num1/num2)

@app.route("/multiple/<int:num1>/<int:num2>")
def multiple(num1, num2):
    return str(num1*num2)

@app.route("/math/<calc>/<int:num1>/<int:num2>")
def calculator (calc, num1, num2):
    if calc == 'add':
      return str(num1*num2)

    if calc == 'subtract':
      return str(num1-num2)

    if calc == 'multiple':
      return str(num1*num2)

    if calc == 'divide':
      if num2 == 0:
        return 'Error - divide by 0:'
      return str(num1/num2)


if __name__ == '__main__':
  app.run(port=5000, debug=True)