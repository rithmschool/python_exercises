from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/calculate")
def calc():
	return render_template("calc.html")

@app.route("/math")
def math():	
	result = None
	num1 = int(request.args.get('num1'))
	num2 = int(request.args.get('num2'))

	if request.args.get('calculation') == "add": 
		result = "the sum is {}".format(num1 + num2)

	elif request.args.get('calculation') == "subtract":
		 result= "the difference is {}".format(num1 - num2)
	
	elif request.args.get('calculation') == "multiply":
		result= "the product is {}".format(num1 * num2)

	elif request.args.get('calculation')== "divide":
		result = "the quotient is {}".format(num1 / num2)
	return render_template("math.html", result=result)					

@app.route("/person/<name>/<int:age>")
def person(name, age):
	name = name
	age = age
	response = "Hello, {}. You are {} years old.".format(name, age)	
	return render_template("person.html", response = response)

if __name__=="__main__":
	app.run(debug=True)
