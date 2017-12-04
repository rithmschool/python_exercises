from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/person/<name>/<age>")
def part1(name,age):
  return render_template("part1.html", name=name,age=age) 

@app.route("/calc")
def calc():
  return render_template("calc.html")

@app.route("/math")
def math():
  num1 = int(request.args.get("num1"))
  num2 = int(request.args.get("num2"))
  total = 0

  if request.args.get("oper") == "add":
    total = num1 + num2
    return render_template("answer.html", total=total)
  if request.args.get("oper") == "subtract":
    total = num1 - num2
    return render_template("answer.html", total=total)
  if request.args.get("oper") == "multiply":
    total = num1 * num2
    return render_template("answer.html", total=total)
  if request.args.get("oper") == "divide":
    total = num1 / num2
    return render_template("answer.html", total=int(total))

  return render_template("answer.html")


if __name__ == ("__main__"):
    app.run(debug=True, port=3000)
