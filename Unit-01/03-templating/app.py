from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/person/<name>/<int:age>')
def person(name, age):
	return render_template('person.html', name=name, age=str(age))

@app.route('/calculate')
def calculate():
	return render_template('calc.html')

@app.route('/math')
def math():
	num1 = int(request.args.get('num1'))
	num2 = int(request.args.get('num2'))
	calculation = request.args.get('calculation')
	
	if calculation == 'add':
		add = num1 + num2
		answer = add
	elif calculation == 'subtract':
		subtract = num1-num2
		answer = subtract
	elif calculation == 'divide':
		try:
			divide = str(num1/num2)
		except ZeroDivisionError:
			divide = "Cannot divide by 0"
		answer = divide
	elif calculation == 'multiply':
		multiply = num1*num2
		answer =  multiply
	
	return render_template('math.html', result=str(answer))


if __name__ == "__main__":
	app.run(port=3000, debug=True)



