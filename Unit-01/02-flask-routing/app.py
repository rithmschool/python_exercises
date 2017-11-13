from flask import Flask

app = Flask(__name__)

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return "{}".format(num1 + num2)

@app.route('/subtract/<int:num1>/<int:num2>')
def subtract(num1, num2):
    return "{}".format(num1 - num2)

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1, num2):
    return "{}".format(num1 * num2)

@app.route('/divide/<int:num1>/<int:num2>')
def divide(num1, num2):
    return "{}".format(num1 / num2)

# Bonus

@app.route('/math/<calc>/<int:num1>/<int:num2>')
def math(calc, num1, num2):
    if calc == 'add':
        return "{}".format(num1 + num2)
    if calc == 'subtract':
        return "{}".format(num1 - num2)
    if calc == 'multiply':
        return "{}".format(num1 * num2)
    if calc == 'divide':
        return "{}".format(num1 / num2)

if __name__ == "__main__":
    app.run(debug=True, port=3000)