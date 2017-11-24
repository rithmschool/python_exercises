from flask import Flask, render_template, request

app = Flask(__name__)

#PART 1
@app.route('/person/<name>/<int:age>')
def person(name, age):
	return render_template('person.html', name=name, age=age)

    
# PART2
@app.route('/calculate')
def calculate():
	return render_template('calc.html')

@app.route('/math', methods=['POST'])
def math():
	num1 = request.form.get('num1')
	num2 = request.form.get('num2')
	if request.form.get('calculation') == 'add':
		value = int(num1) + int(num2)
		return str(value)
	elif request.form.get('calculation') == 'subtract':
		value = int(num1) - int(num2)
		return str(value)
	elif request.form.get('calculation') == 'multiply':
		value = int(num1) * int(num2)
		return str(value)
	elif request.form.get('calculation') == 'divide':
		value = int(num1) / int(num2)
		return str(value)

if __name__ == '__main__':
	app.run(debug=True)