from flask import Flask, render_template, request

app = Flask(__name__)

# PART 1
@app.route('/person/<name>/<int:age>')
def age(name, age):
	return render_template('name.html', name = name, age = age)


# PART 2
@app.route('/calculate')
def calculate():
	return render_template('calculator.html')

@app.route('/math')
def math():
	num1 = int(request.args.get("num1"))
	num2 = int(request.args.get("num2"))
	calculation = request.args.get("calculation")
	math = {
		"add": num1 + num2,
		"subtract": num1 - num2,
		"multiply": num1 * num2,
		"divide": num1 / num2
	}

	output = math.get(calculation)
	return render_template('math.html', output = output)

if __name__ == "__main__":
	app.run(debug = True)