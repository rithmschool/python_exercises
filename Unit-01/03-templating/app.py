from flask import Flask, render_template


app = Flask(__name__)

@app.route('/person/<name>/<int:age>')
def welcome(name, age):
    return render_templae('person.html', name=name, age=age)

@app.route('/calculate')
def calculate():
    return render_template('calc.html')

@app.route('/math')
def math():
    calculation = request.args.get('calculation')
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))

    if calculation == 'add':
        return str(num1+num2)
    elif calculation == 'subtract':
        return str(num1-num2)
    elif calculation == 'multiply':
        return str(num1*num2)
    try:
        quotient = num1 / num2
    except ZeroDivisionError:
        return "Please do not divide by 0"
    return str(quotient)

if __name__ == '__main__':
    app.run(debug=True)
