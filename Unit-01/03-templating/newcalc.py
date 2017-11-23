from flask import Flask
render_template

app = Flask(__name__)

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
	return " {} ".format(num1 + num2)

@app.route('/sub/<int:num1>/<int:num2>')
def subtract(num1, num2):
	return " {} ".format(num1 - num2)

@app.route('/divide/<int:num1>/<int:num2>')
def division(num1, num2):
	return " {} ".format(num1 / num2)

@app.route('/mult/<int:num1>/<int:num2>')
def multiply(num1, num2):
	return " {} ".format(num1 * num2)

@app.route('/calculate')
def calculator():
	return render_template("calc.html")

if __name__ == "__main__":
    app.run(debug=True)
