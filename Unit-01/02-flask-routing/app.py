# from the flask library import a class named Flask
from flask import Flask

# create an instance of the Flask class
app = Flask(__name__)

@app.route('/add/<num1>/<num2>')
def add(num1, num2):
	try:
		num1 = int(num1)
		num2 = int(num2)
	except ValueError:
		num1 = float(num1)
		num2 = float(num2)

	sum = num1 + num2
	return str(sum)

@app.route('/subtract/<num1>/<num2>')
def subtract(num1, num2):
	try:
		num1 = int(num1)
		num2 = int(num2)
	except ValueError:
		num1 = float(num1)
		num2 = float(num2)

	diff = num1 - num2
	return str(diff)

@app.route('/multiply/<num1>/<num2>')
def multiply(num1, num2):
	try:
		num1 = int(num1)
		num2 = int(num2)
	except ValueError:
		num1 = float(num1)
		num2 = float(num2)

	multiply = num1 * num2
	return str(multiply)

@app.route('/divide/<num1>/<num2>')
def divide(num1, num2):
	try:
		num1 = int(num1)
		num2 = int(num2)
	except ValueError:
		num1 = float(num1)
		num2 = float(num2)

	divide = num1 / num2
	return str(divide)

if __name__ == "__main__":
	app.run(debug=True,port=3000)