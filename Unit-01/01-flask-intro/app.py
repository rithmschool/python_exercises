from flask import Flask 

app = Flask(__name__)


# have a route for /welcome, which responds with the string "welcome"
# have a route for /welcome/home, which responds with the string
# "welcome home" have a route for /welcome/back, which responds with the
# string "welcome back" Bonus

# Add another route to /sum and inside the function which sends a response, create a variable called sum which is equal to 5+5. Respond with the sum variable.

@app.route('/welcome')
def welcome():
	return 'welcome'

@app.route('/welcome/home')
def welcome_home():
	return 'welcome home'

@app.route('/welcome/back')
def welcome_back():
	return "welcome back"

@app.route('/sum')
def sum():
	sum = 5 + 5
	return str(sum)

if __name__ == "__main__":
	app.run(debug=True, port=3000)