from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello World!"

@app.route("/add/<int:a>/<int:b>")
def add(a,b):
	return str(a+b)

@app.route("/subtract/<int:a>/<int:b>")
def subtract(a,b):
	return str(a-b)

@app.route("/multiply/<int:a>/<int:b>")
def multipy(a,b):
	return str(a*b)

@app.route("/divide/<int:a>/<int:b>")
def divide(a,b):
	try: a/b
	except ZeroDivisionError:
		return "Cannot divide by zero"
	return str(a/b)

@app.route("/math/<operation>/<int:a>/<int:b>")
def calc(operation, a, b):
	if operation == "add":
		return str(a+b)
	if operation == "subtract":
		return str(a-b)
	if operation == "multiply":
		return str(a*b)
	if operation == "divide":
		try: a/b
		except ZeroDivisionError:
			return "Cannot divide by zero"
		return str(a/b)

if __name__ == "__main__":
	app.run(debug=True)