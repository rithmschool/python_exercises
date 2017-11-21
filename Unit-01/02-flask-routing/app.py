from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  return "You are in the right place"

@app.route("/<opp>/<num1>/<num2>")
def do_math(opp, num1, num2):
  if opp == "add":
    return str(int(num1) + int(num2))
  elif opp == "subtract":
    return str(int(num1) - int(num2))
  elif opp == "multiply":
    return str(int(num1) * int(num2))
  elif opp == "divide":
    return str(float(num1) / int(num2))
	
@app.route("/math/<opp>/<num1>/<num2>")
def do_math2(opp, num1, num2):
  if opp == "add":
    return str(int(num1) + int(num2))
  elif opp == "subtract":
    return str(int(num1) - int(num2))
  elif opp == "multiply":
    return str(int(num1) * int(num2))
  elif opp == "divide":
    return str(float(num1) / int(num2))

if __name__ == "__main__":
  app.run(debug = True)