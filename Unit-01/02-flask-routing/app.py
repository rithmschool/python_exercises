# from the flask library import a class named Flask
from flask import Flask

# create an instance of the Flask class
app = Flask(__name__)

@app.route('/math/<op>/<num1>/<num2>')
def operation(op, num1, num2):
	operation = 0
	try:
		num1 = int(num1)
		num2 = int(num2)
	except ValueError:
		num1 = float(num1)
		num2 = float(num2)

	if op == 'add':
		operation = num1 + num2
	elif op == 'subtract':
		operation = num1 - num2
	elif op == 'multiply':
		operation = num1 * num2
	elif op == 'divide':
		try:
			operation = num1 / num2
		except ZeroDivisionError:
			return "Infinity"

	return str(operation)

@app.route('/<op>/<num1>/<num2>')
def add(op, num1, num2):
	operation = 0
	try:
		num1 = int(num1)
		num2 = int(num2)
	except ValueError:
		num1 = float(num1)
		num2 = float(num2)

	if op == 'add':
		operation = num1 + num2
	elif op == 'subtract':
		operation = num1 - num2
	elif op == 'multiply':
		operation = num1 * num2
	elif op == 'divide':
		try:
			operation = num1 / num2
		except ZeroDivisionError:
			return "Infinity"

	return str(operation)

if __name__ == "__main__":
	app.run(debug=True,port=3000)