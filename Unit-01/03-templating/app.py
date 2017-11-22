from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route("/person/<name>/<int:age>")
def show_person(name, age):
	return render_template("person.html", name = name, age=age)

@app.route("/calculate")
def show_calc():
	return render_template("calc.html")

#Practice to do it a GET
# @app.route("/math")
# def do_math():
# 	num1 = int(request.args.get("num1"))
# 	num2 = int(request.args.get("num2"))
# 	opp = request.args.get("opp")
# 	if opp == "add":
# 		answer =  num1 + num2
# 	elif opp == "subtract":
# 		answer =  num1 - num2
# 	elif opp == "multiply":
# 		answer =  num1 * num2
# 	elif opp == "divide":
# 		answer =  num1 / num2
# 	return render_template("math.html", answer=answer)

#Done with a POST
@app.route("/math", methods=["POST"])
def do_math():
	num1 = int(request.form.get("num1"))
	num2 = int(request.form.get("num2"))
	opp = request.form.get("opp")
	if opp == "add":
		answer =  num1 + num2
	elif opp == "subtract":
		answer =  num1 - num2
	elif opp == "multiply":
		answer =  num1 * num2
	elif opp == "divide":
		answer =  num1 / num2
	return render_template("math.html", answer=answer)

if __name__ == "__main__":
	app.run(debug=True)