from flask import Flask
app = Flask(__name__)


@app.route('/add/<int:a>/<int:b>')
def add(a=5,b=5):
	return str(a+b)

@app.route('/subtract/<int:a>/<int:b>')
def subtract(a=5,b=5):
	return str(a-b)

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a=5,b=5):
	return str(a * b)

@app.route('/divide/<int:a>/<int:b>')
def divide(a=5,b=5):
	return str(a/b)

@app.route('/math/<operation>/<int:num1>/<int:num2>')
def math(operation="add", num1=5, num2=5):
	if operation == "add":
		return str(num1+num2)
	if operation == "subtract":
		return str(num1-num2)
	if operation == "multiply":
		return str(num1*num2)
	if operation == "divide":
		return str(num1/num2)
		# operations = {
		# "add": add,
		# "subtract": subtract,
		# "multiply": multiply,
		# "divide": divide
		# }

		# return operations[operation](num1,num2)

if __name__ == '__main__':
	app.run(port=3000, debug=True)