from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
	return ""

# @app.route("/add/<int:number1>/<int:number2>")
# def add(number1,number2):
# 	return str(number1 + number2)

# @app.route("/subtract/<int:number1>/<int:number2>")
# def subtract(number1,number2):
# 	return str(number1 - number2)

# @app.route("/multiply/<int:number1>/<int:number2>")
# def multiply(number1,number2):
# 	return str(number1 * number2)

# @app.route("/divide/<int:number1>/<int:number2>")
# def divide(number1,number2):
# 	return str(number1 / number2)

@app.route("/<string:operation>/<int:number1>/<int:number2>")
def perform_math_function(operation,number1,number2):
	answer = None
	if operation == "add":
		answer = number1 + number2
	elif operation == "subtract":
		answer = number1 - number2
	elif operation == "multiply":
		answer = number1 * number2
	elif operation == "divide":
		answer = number1 / number2
	else:
		return "invalid operation"

	return str(answer)


app.run(debug=True)