from flask import Flask, render_template, request
import requests
import bs4

app = Flask(__name__)

@app.route('/')
def display_keyword_form():
  return render_template('keyword.html')

@app.route('/results')
def get_results():
  keyword = request.args.get('keyword')
  data = requests.get('https://news.google.com/')
  soup = bs4.BeautifulSoup(data.text, 'html.parser')
  headlines = soup.select('.titletext')

  lst_headlines = [headline for headline in headlines]
  lst_results = []

  for headline in lst_headlines:
    if headline.text.find(keyword) > -1:
      headline_txt = headline.text
      headline_link = headline.find_parent('a').get('href')
      lst_results.append([headline_txt, headline_link])

  return render_template('results.html', lst_results=lst_results, keyword=keyword)

@app.route('/person/<name>/<age>')
def display_person_info(name, age):
  return render_template('person.html', name=name, age=age)

@app.route('/calculate')
def calculate():
  return render_template('calc.html')

@app.route('/math')
def math():
  operation = request.args.get('calculation')
  num1 = int(request.args.get('num1'))
  num2 = int(request.args.get('num2'))
  if operation == 'add':
    return str(num1 + num2)
  if operation == 'subtract':
    return str(num1 - num2)
  if operation == 'multiply':
    return str(num1 * num2)
  if operation == 'divide':
    if num2 == 0:
      return "0"
    return str(num1/num2)

if __name__ == "__main__":
  app.run(debug=True, port=4000)