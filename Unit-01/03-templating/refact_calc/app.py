from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def welcome():
  return "Welcome to my app"


@app.route("/calculate")
def calc():
	return render_template("calc.html")

@app.route("/math")
def math():
    num1 = int(request.args['num1'])
    num2 = int(request.args['num2'])
    select = request.args['select']
   
    if  select == 'add':
        return "The sum of " + str(num1) + " + " + str(num2) + " is " + str(num1 + num2)
    if  select == "subtruct":   
        return "The substruction of " + str(num1) + " - " + str(num2) + " is " +  str(num1 - num2)
    if  select == "multiply":
        return "The product of " + str(num1) +  " * " + str(num2) + " is " + str(num1 * num2)
    if  select == "divide":
        return "The divition of " + str(num1) + " / " + str(num2) + " is " + str(round((num1 / num2),2))



if __name__ == "__main__":
  app.run(port=8080, debug=True)