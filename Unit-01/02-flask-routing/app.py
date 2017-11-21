from flask import Flask

app= Flask(__name__)

@app.route("/math/<operation>/<num1>/<num2>")
def do_math(operation, num1, num2):
	if operation == "addition":
		output = int(num1) + int(num2)
	elif operation == "subtraction":
		output = int(num1) - int(num2)
	elif operation == "multiplication":
		output = int(num1) * int(num2)
	elif operation == "division":
		if int(num2) == 0:
			output = "error: do not divide by zero"
		else:
			output = int(num1) / int(num2)
	else:
		output = "valid operations are addition, subtraction, multiplication, and division"
	return f"{output}"				


if __name__ == "__main__":
	app.run(debug=True,port=3000)		
