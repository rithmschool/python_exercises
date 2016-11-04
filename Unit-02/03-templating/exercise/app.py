from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def root():
	return render_template("index.html")


#######################################################
# Part 1

@app.route("/person/<name>/<age>")
def person(name, age):
	return render_template("person.html", name=name, age=age)

#######################################################
# Part 2

@app.route("/calculate")
def calculate():
	return render_template("calc.html")


@app.route("/math")
def math():
	_results = None
	operations = {"add": lambda x,y : x+y, 
		"subtract": lambda x,y : x-y, 
		"multiply": lambda x,y : x*y, 
		"divide": lambda x,y : x/y}
	number1 = int(request.args.get('num1'))
	number2 = int(request.args.get('num2'))
	operation = request.args.get("operation")
	_results = str(operations[operation](number1,number2))
	return render_template("math.html", results=_results)


app.run(debug=True)