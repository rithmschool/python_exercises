from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/person/<name>/<int:age>")
def person(name, age):
	return render_template("person.html", name=name, age=age)

@app.route("/calculate")
def calc():
	return render_template("calc.html")

@app.route("/math")
def math():
	calculation = request.args.get("calculation")
	num1 = int(request.args.get("num1"))
	num2 = int(request.args.get("num2"))
	if calculation == "add":
		return str(num1+num2)
	elif calculation == "subtract":
		return str(num1-num2)
	elif calculation == "multiply":
		return str(num1*num2)
	try: num1/num2
	except ZeroDivisionError:
		return "Cannot divide by zero"
	return str(num1/num2)

if __name__ == "__main__":
	app.run(debug=True)