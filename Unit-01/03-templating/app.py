# from the flask library import a class named Flask
from flask import Flask, render_template, request

# create an instance of the Flask class
app = Flask(__name__)

@app.route('/person/<name>/<age>')
def name_and_age(name, age):
	return render_template('age.html', name=name, age=age)

@app.route('/calculate')
def calculate():
	return render_template('calc.html')

@app.route('/math')
def math():
	result = 0
	num1 = request.args.get('num1')
	num2 = request.args.get('num2')

	try:
		num1 = int(num1)
		num2 = int(num2)
	except ValueError:
		num1 = float(num1)
		num2 = float(num2)

	calculation = request.args.get('calculation')

	if calculation == 'add':
		result = num1 + num2
	elif calculation == 'subtract':
		result = num1 - num2
	elif calculation == 'multiply':
		result = num1 * num2
	elif calculation == 'divide':
		try:
			result = round(num1 / num2, 2)
		except ZeroDivisionError:
			return "Infinity"

	return render_template('result.html', result=result)

if __name__ == "__main__":
	app.run(debug=True,port=3000)