from flask import Flask

app = Flask(__name__)

@app.route("/math/<fn>/<int:num1>/<int:num2>")
@app.route("/<fn>/<int:num1>/<int:num2>")
def calculator(fn, num1, num2):
	if fn == "add":
		return str(num1 + num2)
	elif fn == "subtract":
		return str(num1 - num2)
	elif fn == "multiply":
		return str(num1 * num2)
	elif fn == "divide":
		return str(num1 / num2)
	else:
		return "Inputs invalid"

if __name__ == "__main__":
	app.run(debug=True, port=3000)