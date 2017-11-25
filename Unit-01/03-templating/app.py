from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/person/<name>/<age>")
def show(name, age):
	return render_template('person-name-age-show.html', name = name, age = age)

@app.route("/calculate")
def calculate():
	return render_template('calc.html')

@app.route("/math")
def math():
	num1 = float(request.args.get('num1'))
	num2 = float(request.args.get('num2'))
	calculation = request.args.get('calculation')
	result = calculateNums(num1, num2, calculation)
	return render_template('math.html', result=result)



def calculateNums (number1=0, number2=0, operator='add'):
	if operator == "add":
		return number1 + number2
	elif operator == "subtract":
		return number1 - number2
	elif operator == "multiply":
		return number1 * number2
	elif operator == "divide":
		return number1 / number2			


if __name__ == '__main__':
	app.run(debug=True)	