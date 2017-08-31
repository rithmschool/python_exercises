from flask import Flask

app = Flask(__name__)

@app.route('/addition/<int:num1>/<int:num2>')
def addition(num1, num2):
	total = num1 + num2
	return str(total)

@app.route('/subtraction/<int:num1>/<int:num2>')
def subtraction(num1, num2):
	difference = num1 - num2
	return str(difference)

@app.route('/multiplication/<int:num1>/<int:num2>')
def multiplication(num1, num2):
	product = num1 * num2
	return str(product)

@app.route('/divide/<int:num1>/<int:num2>')
def divide(num1, num2):
	try:
		quotient = num1 / num2
	except ZeroDivisionError:
		return "Please do not divide by 0"
	return str(quotient)

@app.route('/math/<calculation>/<int:num1>/<int:num2>')	
def calcs(calculation, num1, num2):
	if calculation == 'add':
		return str(num1 + num2)
	elif calculation == 'subtract':
		return str(num1 - num2)
	elif calculation == 'multiply':
		return str(num1 * num2)
	try:
		quotient = num1 / num2
	except ZeroDivisionError:
		return "Please do not divide by 0"
	return str(quotient)
	

if(__name__) == "__main__":
	app.run(debug=True, port=3000)