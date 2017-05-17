from flask import Flask, render_template, request
import urllib.request
import bs4
import csv

app = Flask(__name__)

@app.route('/person/<name>/<age>')
def display_name_age(name, age):
	return render_template('base.html', name=name, age=age)

@app.route('/calculate')
def show_form():
	return render_template('calc.html')

@app.route('/math')
def calculate():
	num1 = int(request.args.get('num1'))
	num2 = int(request.args.get('num2'))
	operation = request.args.get('calculation')
	if operation == 'add':
		return str(num1 + num2)
	elif operation == 'subtract':
		return str(num1 - num2)
	elif operation == 'multiply':
		return str(num1 * num2)
	elif operation == 'divide':
		return str(num1 / num2)

@app.route('/')
def search():
	return render_template('googlenews_form.html')

@app.route('/results')
def show_results():
	url = 'https://news.google.com/'
	data = urllib.request.urlopen(url).read()
	soup = bs4.BeautifulSoup(data, "html.parser")
	a_blocks = soup.select('.esc-lead-article-title a')
	titles = [val.select(".titletext")[0].text for val in a_blocks]
	links = [val['href'] for val in a_blocks]
	correct_links = {}
	for idx, title in enumerate(titles):
		if request.args.get('keyword') in title:
			correct_links[title] = links[idx]
	# from IPython import embed; embed()
	return render_template('results.html', correct_links=correct_links)



if __name__ == '__main__':
	app.run(debug=True)