from flask import Flask, render_template, request
import bs4
import requests

app = Flask(__name__)

@app.route("/")
def scrape_form():
	return render_template("scrape.html")

@app.route("/results")
def headlines():
	query = request.args.get("query_string")
	r = requests.get("https://news.google.com/?q=" + query)
	soup = bs4.BeautifulSoup(r.text, "html.parser")

	headlines = soup.select(".titletext")
	url_head = soup.select(".esc-lead-article-title a")
	headlines_list = []

	for val in headlines:
		headlines_list.append(val.text)

	return render_template("results.html", keywords=headlines_list)



@app.route("/person/<name>/<age>")
def person_details(name,age):
	return render_template("person.html", person_name=name, person_age=age)

@app.route("/calculate")
def calculate_equation():
	return render_template("calc.html")

@app.route("/math")
def calculator():
	number_one = int(request.args.get("num1"))
	number_two = int(request.args.get("num2"))
	operator = request.args.get("calculation")
	if operator == "add":
	 	return str(number_one + number_two)
	elif operator == "subtract":
	 	return str(number_one - number_two)
	elif operator == "multiply":
	 	return str(number_one * number_two)
	elif operator == "divide":
	 	return str(number_one / number_two)
	else:
	 	return "Inputs invalid"


if __name__ == "__main__":
	app.run(debug=True, port=3000)