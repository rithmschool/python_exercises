from flask import Flask

app = Flask(__name__)

@app.route("/<operation>/<int:num1>/<int:num2>")
def math(operation, num1, num2):
	math = {
		"addition": num1 + num2,
		"subtraction": num1 - num2,
		"multiplication": num1 * num2,
		"division": num1 / num2
	}
	return str(math[operation])

if __name__ == "__main__":
	app.run(port = 8080, debug = True)