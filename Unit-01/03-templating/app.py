from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    names_of_instructors = ['Elie', 'Tim', 'Matt']
    random_name = 'Tom'
    return render_template('index.html', names=names_of_instructors, name=random_name)

@app.route('/second')
def second():
    return 'this'


@app.route('/title')
def title():
    return render_template('title.html')

@app.route('/index')
def test_index():
    return render_template('index.html')

@app.route('/data')
def print_name():
    first = request.args.get('first')
    last = request.args.get('second')
    return "You put {} {}".format(first, last)

@app.route('/person/<name>/<age>')
def print_something(name, age):
    return render_template('person.html', name=name, age=age)

@app.route('/calculate')
def my_calc():
    return render_template('calc.html')


@app.route('/math')
def my_math():
        num = int(request.args.get('num'))
        num2 = int(request.args.get('num2'))
        operation = request.args.get('operation')

        if operation == 'add':
            return str(num + num2)
        if operation == 'sub':
            return str(num - num2)
        if operation == 'multi':
            return str(num * num2)
        try:
            divi = num / num2
        except ZeroDivisionError:
            return 'Please do not divide by 0'
        return str(divi)
if __name__ == '__main__':
    app.run(debug=True)
