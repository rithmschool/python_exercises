from flask import Flask, render_template, request, url_for

app = Flask(__name__)


# Part 1
@app.route('/person/<name>/<int:age>')
def say_name_and_age(name, age):
	name = name.title()
	return render_template('person.html', name=name, age=age)
	
# Part 2
@app.route('/calculate')
def calc():
	return render_template('calc.html')

@app.route('/math')
def math():
	calculation = request.args.get('calculation')
	num1 = int(request.args.get('num1'))
	num2 = int(request.args.get('num2'))

	if calculation == 'add':
		return "The sum is: " + str(num1 + num2)
	elif calculation == 'subtract':
		return "The difference is: " + str(num1 - num2)
	elif calculation == 'multiply':
		return "The product is: " + str(num1 * num2)
	elif calculation == 'divide':
		return "The quotient is: " + str(num1 / num2)

if __name__ == "__main__":
	app.run(debug=True)