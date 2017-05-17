from flask import Flask, render_template

app = Flask(__name__)

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
	return str(num1 + num2)

@app.route('/subtract/<int:num1>/<int:num2>')
def subtract(num1, num2):
	return str(num1 - num2)

@app.route('/multiply/<int:num1>/<int:num2>')
def mutiply(num1, num2):
	return str(num1 * num2)

@app.route('/divide/<int:num1>/<int:num2>')
def divide(num1, num2):
	return str(num1 / num2)

@app.route('/math/<operation>/<int:num1>/<int:num2>')
def math(operation, num1, num2):
	if operation == 'add':
		return str(num1 + num2)
	elif operation == 'subtract':
		return str(num1 - num2)
	elif operation == 'multiply':
		return str(num1 * num2)
	elif operation == 'divide':
		return str(num1 / num2)

if __name__ == '__main__':
	app.run()