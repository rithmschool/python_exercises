from flask import Flask, render_template, request
import urllib.request
import bs4
import re

app =  Flask(__name__)

@app.route('/person/<name>/<age>')
def person(name, age):
    return render_template('person.html', name=name, age=age)

@app.route('/calculate')
def calculate():
    return render_template('calc.html')

@app.route('/math')
def do_math():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    if request.args.get('calculation') == 'add':
        result = num1 + num2
    if request.args.get('calculation') == 'subtract':
        result = num1 - num2
    if request.args.get('calculation') == 'multiply':
        result = num1 * num2
    if request.args.get('calculation') == 'divide':
        result = num1 / num2        
    
    return "{}".format(result)

@app.route('/')
def root():
    return render_template('form.html')

@app.route('/results')
def results():
    keyword = request.args.get('keyword')
    url = 'https://news.google.com'
    data = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(data, 'html.parser')

    links = soup.find_all('a', role='heading', string=re.compile(keyword))
    links_length = len(links)

    return render_template('results.html', links=links, links_length=links_length)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
