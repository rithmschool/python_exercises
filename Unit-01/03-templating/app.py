from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hi():
	return "Hi there"
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/person/<name>/<age>')
def person(name,age):
	return render_template('index.html', name=name, age=age)

def add(a=5,b=5):
	return str(a+b)

def subtract(a=5,b=5):
	return str(a-b)

def multiply(a=5,b=5):
	return str(a * b)

def divide(a=5,b=5):
	return str(a/b)

@app.route('/calculate')
def calc():
	return render_template('calculate.html')

@app.route('/math')
def math():
	operations = {
		"add": add,
		"subtract": subtract,
		"multiply": multiply,
		"divide": divide
		}

	return operations[request.args['operation'].lower()](int(request.args["num1"]), int(request.args["num2"]))
		# return operations[](int(request.args["num1"]), int(request.args["num2"]))
	# return render_template('calculate.html', num1=num1, num2=num2, operation=operation)


if __name__ == '__main__':
	app.run(port=3000,debug=True)