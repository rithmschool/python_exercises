from flask import Flask
app = Flask(__name__)

@app.route('/add/<int:a>/<int:b>')
def add(a,b):
	add = a+b
	return str(add)

@app.route('/divide/<int:a>/<int:b>')
def divide(a,b):
	try:
		divide = a/b
	except ZeroDivisionError:
		return "Cannot divide by 0"
	return str(divide)

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a,b):
	multiply = a*b
	return str(multiply)

@app.route('/subtract/<int:a>/<int:b>')
def subtract(a,b):
	subtract = a-b
	return str(subtract)

@app.route('/math/<path>/<int:a>/<int:b>')
def math(path,a,b):
	if path == 'add':
		return str(a+b)
	elif path == 'subtract':
		return str(a-b)
	elif path == 'divide':
		try:
			return str(a/b)
		except ZeroDivisionError:
			return "Cannot divide by 0"
	elif path == 'multiply':
		return str(a*b)


if __name__ == "__main__":
	app.run(port=3000, debug=True)
