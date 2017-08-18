from flask import Flask, render_template, url_for, request
# create an instance of the Flask class
app = Flask(__name__)

@app.route('/person/<name>/<int:age>')
def makeURL(name,age):
	return render_template('heir.html',name=name, age=age)

@app.route('/calculate')
def make_form():
	return render_template('calc.html')

@app.route('/math/')
def math():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    calculation = request.args.get('calculation')
    if calculation == 'add':
    	return str(num1+num2)
    elif calculation == 'subtract':
    	return str(num1-num2)
    elif calculation == 'multiply':
    	return str(num1*num2)
    elif calculation == 'divide':
    	return str(num1/num2)

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

#so you only start the server once and only start when running app.py
if __name__ == "__main__":
	app.run(debug=True)

