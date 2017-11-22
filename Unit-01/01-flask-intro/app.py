from flask import Flask, render_template

app = Flask(__name__)

@app.route("/welcome")
def welcome():
	return render_template("index.html")

@app.route("/welcome/home")
def welcome_home():
	return render_template("home.html")

@app.route("/welcome/back")
def welcome_back():
	return render_template("back.html")	

@app.route("/sum")
def sum_fn():
	sum_num = 5 + 5 
	return render_template("sum.html", sum = sum_num)

if __name__ == "__main__":
	app.fun(debug=True)	
