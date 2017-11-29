from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/person/<name>/<age>')
def print_name(name, age):
	return render_template('hey_person.html', name=name, age=age)
    

@app.route('/calculator')
def calculator():
    return render_template('calc.html')


@app.route('/math')
def math():
  num1 = int(request.args.get('num1'))
  num2 = int(request.args.get('num2'))
  op = request.args.get('operator')
  if op == '+':
      return f"{num1 + num2}"
  if op == '-':
      return f"{num1 - num2}"
  if op == '*':
      return f"{num1 * num2}" 
  if op == '/':
      return f"{math.floor(num1 / num2)}"



if __name__ == "__main__":
	app.run(debug=True)
