from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/calculate')
def calculate():
    return render_template('calc.html')

@app.route('/math', methods=['POST'])
def math():
    operation = request.form['operation']
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])

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
        try:
            result = num1 / num2
        except ZeroDivisionError:
            answer = 'Division by zero is not allowed.'
            return render_template('result.html', answer=answer)

    answer = "{} {} {} = {}".format(num1, verb, num2, result)

    return render_template('result.html', answer=answer)

if __name__ == "__main__":
    app.run(port=3000, debug=True)
