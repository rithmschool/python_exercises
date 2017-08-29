# Part 1:
# base.html created in templates directory
# route for /person/<name>/<age>

from flask import Flask, render_template, request
import requests
import bs4
import jinja2

app = Flask(__name__)

app.jinja_env.undefined = jinja2.StrictUndefined
app.jinja_env.auto_reload = True

@app.route('/person/<name>/<int:age>')
def name_and_age(name, age):
    return render_template('nameage.html', name=name, age=age)

@app.route('/calculate')
def display_calc():
    return render_template('calc.html')

# Part 2 - Calculator App Refactor
def add(a, b):
    return str(a + b)

def subtract(a, b):
    return str(a - b)

def multiply(a, b):
    return str(a * b)

def divide(a, b):
    return str(a / b)

@app.route('/math')
def math_calc():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    calculation = request.args.get('calculation')

    if calculation == "add":
        return add(num1, num2)
    if calculation == "subtract":
        return subtract(num1, num2)
    if calculation == "multiply":
        return multiply(num1, num2)
    if calculation == "divide":
        return divide(num1, num2)

# Part 3 - Google News by keyword
@app.route('/')
def root():
    return render_template('keyword.html')

@app.route('/results')
def results():
    keyword = request.args.get('keyword') # results are case-sensitive!
    r = requests.get('https://news.google.com')
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    headlines = soup.select('.esc-lead-article-title')
    # links = soup.select('.esc-lead-article-title h2 a')
    headline_list = []
    # links_list = []
    for headline in headlines:
        headline_list.append(headline.text)
    # for link in links:
    #     links_list.append(link.text)

    def find_headline_by_keyword(word):
        return [title for title in headline_list if word in title]

    return render_template('results.html', title_list=find_headline_by_keyword(keyword))

if __name__ == '__main__':
    app.run(port=3000)