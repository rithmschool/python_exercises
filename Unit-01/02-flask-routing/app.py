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
	return "{}".format(int(num1 / num2))

@app.route('/math/<operation>/<int:num1>/<int:num2>')
def math(operation, num1, num2):
	if operation == 'add':
		return "{}".format(num1 + num2)
	if operation == 'subtract':
		return "{}".format(num1 - num2)
	if operation == 'multiply':
		return "{}".format(num1 * num2)
	if operation == 'divide':
		return "{}".format(int(num1 / num2))

if __name__ == '__main__':
	app.run()