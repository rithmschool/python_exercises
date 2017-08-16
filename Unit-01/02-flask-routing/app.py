from flask import Flask

app = Flask(__name__)

@app.route('/add/<int:num_1>/<int:num_2>')
def add(num_1, num_2):
    return str(num_1 + num_2)
#
@app.route('/subtract/<int:num_1>/<int:num_2>')
def subtract(num_1, num_2):
    return str(num_1 - num_2)

@app.route('/multiply/<int:num_1>/<int:num_2>')
def multiply(num_1, num_2):
    return str(num_1 * num_2)

@app.route('/divide/<int:num_1>/<int:num_2>')
def divide(num_1, num_2):
    try:
        quotient = num_1 /num_2
    except ZeroDivisionError:
        return "Please do not divide by 0"
    return str(quotient)
#
@app.route('/math/<calculator>/<int:num_1>/<int:num_2>')
def math_functions(calculator, num_1,num_2):
    if calculator == "add":
        return str(num_1 + num_2)
    elif calculator == "subtract":
        return str(num_1 - num_2)
    elif calculator == "multiply":
        return str(num_1 * num_2)
    try:
        quotient = num_1 / num_2
    except ZeroDivisionError:
        return "🚯"
    return str(quotient)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
