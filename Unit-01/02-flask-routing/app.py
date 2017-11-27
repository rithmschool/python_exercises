from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def welcome():
  return "Welcome to my app"

# @app.route("/add/<int:num1>/<int:num2>")
# def add(num1, num2):
#   return f"The sum of {num1} + {num2} is {num1 + num2}" 

# @app.route("/multiply/<int:num1>/<int:num2>")
# def multiply(num1, num2):
#   return f"The product of {num1} * {num2} is {num1 * num2}"

# @app.route("/divide/<int:num1>/<int:num2>")
# def divide(num1, num2):
#   return f"The divition of {num1} / {num2} is {num1 / num2}"

# @app.route("/substruct/<int:num1>/<int:num2>")
# def substruct(num1, num2):
#   return f"The substruction of {num1} - {num2} is {num1 - num2}" 

@app.route("/calculate")
def calc():
	return render_template("calc.html")

@app.route("/math")
def math():
    num1 = int(request.args['num1'])
    num2 = int(request.args['num2'])
    select = request.args['select']
    if  select == 'add':
        return "The sum of " + "num1" + " + " + "num2" + " is " + str(num1 + num2) 
    if  select == "subtruct":	
        return "The substruction of " + "num1" + " - " + "num2" + " is " +  str(num1 - num2) 
    if  select == "multiply":
        return "The product of " + "num1" +  " * " + "num2" + " is " + str(num1 * num2)
    if  select == "divide":
        return "The divition of " + "num1" + " / " + "num2" + " is " + str(round((num1 / num2),2))



if __name__ == "__main__":
  app.run(port=8080, debug=True)