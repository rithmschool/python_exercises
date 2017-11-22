from flask import Flask

app = Flask(__name__)

# @app.route('/add/<int:num>/<int:num2>')
# def add(num, num2):
# 	return str(num + num2)

# @app.route('/subtract/<int:num>/<int:num2>')
# def subtract(num, num2):
# 	return str(num - num2)

# @app.route('/divide/<int:num>/<int:num2>')
# def divide(num, num2):
# 	return str(num / num2)

# @app.route('/multiply/<int:num>/<int:num2>')
# def multiply(num, num2):
# 	return str(num * num2)

@app.route('/math/<operation>/<int:num>/<int:num2>')
def math(operation, num, num2):
	if operation == 'add':
		return str(num + num2)
	if operation == 'subtract':
		return str(num - num2)
	if operation == 'divide':
		return str(num / num2)
	if operation == 'multiply':
		return str(num * num2)
	else:
		return 'Invalid Input!'

if __name__ == '__main__':
	app.run(debug=True)