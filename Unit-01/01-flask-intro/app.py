from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome():
	return "welcome"

@app.route('/welcome/home')
def welcome_home():
	return "welcome home"

@app.route('/welcome/back')
def welcome_back():
	return "welcome back"

@app.route('/sum')
def make_sum():
	my_sum = 5+5
	return str(my_sum)

if __name__ == "__main__":
	app.run(debug=True,port=3000)