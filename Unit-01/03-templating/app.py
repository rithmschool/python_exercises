import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template, request



app = Flask(__name__)


@app.route('/calculate')
def calc():
    return render_template('calculate.html')

@app.route('/')
def welcome():
    names_of_instructors = ["Elie", "Tim", "Matt"]
    random_name = "Tom"
    return render_template('index.html', names=names_of_instructors, name=random_name)

@app.route('/second')
def second():
    return "WELCOME TO THE SECOND PAGE!"

@app.route('/title')
def title():
    return render_template('title.html')

# we need a route to render the form
@app.route('/show-form')
def show_form():
    return render_template('first_form.html')

# we need to do something when the form is submitted
@app.route('/data')
def print_name():
    first = request.args.get('first')
    last = request.args.get('last')
    return "You put {} {}".format(first, last)

@app.route('/math')
def mathy():
    calculation = request.args.get('calculation')
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))

    if calculation == 'add':
        return str(num1 + num2)
    elif calculation == 'subtract':
        return str(num1 - num2)
    elif calculation == 'multiply':
        return str(num1 * num2)
    elif calculation == 'divide':
        return str(num1 / num2)


@app.route('/person/<name>/<age>')
def show_name_age(name, age):
    return render_template('name_age.html', names=name, ages=age)





if __name__ == '__main__':
    app.run(debug=True, port = 3000)