from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the calculator!"


@app.route('/math/<operation>/<int:num1>/<int:num2>')
def math(operation, num1, num2):
    result = 0

    if operation == 'add':
        result = num1 + num2
        verb = 'plus'
    if operation == 'subtract':
        result = num1 - num2
        verb = 'minus'
    if operation == 'multiply':
        result = num1 * num2
        verb = 'times'
    if operation == 'divide':
        verb = 'divided by'
        if num2 == 0:
            return 'Division by zero is not allowed.'
        else:
            result = num1 / num2

    return "{} {} {} = {}".format(num1, verb, num2, result)


if __name__ == "__main__":
    app.run(port=3000, debug=True)
