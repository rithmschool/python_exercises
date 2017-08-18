# from the flask library import a class named Flask
from flask import Flask

# create an instance of the Flask class
app = Flask(__name__)

# listen for a route to `/` - this is known as the root route
@app.route('/')
# when this route is reached (through the browser bar or someone clicking a link, run the following function)
def hello():
    # this `return` is the response from our server. We are responding with the text "Hello World"
	return "Hello World!"

@app.route('/<number1>/<number2>')
def welcome(number1,number2):
	what_I_want = int(number1) + int(number2)
	return str(what_I_want)

@app.route('/math/<calculation>/<int:num1>/<int:num2>')
def mathz(calculation,num1,num2):
	if calculation == 'add':
		return str(num1+num2)
	elif calculation == 'subtract':
		return str(num1-num2)
	elif calculation == 'multiply':
		return str(num1*num2)
	elif calculation == 'divide':
		return str(num1/num2)


@app.route('/welcome')
def response():
	return 'welcome!'

@app.route('/welcome/home')
def again():
	return 'welcome home'

@app.route('/welcome/back')
def yo():
	return 'welcome back'

@app.route('/sum')
def sum_time():
	my_sum = 5+5
	return str(my_sum)


#so you only start the server once and only start when running app.py
if __name__ == "__main__":
	app.run(debug=True,port=3000)


