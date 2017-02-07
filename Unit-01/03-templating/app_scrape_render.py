import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template, request



app = Flask(__name__)
url = 'https://news.google.com'
data = requests.get(url)
soup = BeautifulSoup(data.text, "html.parser")


titles = soup.select("span.titletext")
links = soup.select(".article ")


results = [{'title': title.text,
  'link': title.parent['href']} for title in titles]






@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/result')
def res():
    key_word = request.args.get('keyword')
    headlines = [result for result in results if result['title'].find(key_word) > -1]

    return render_template('result.html', headlines=headlines)


if __name__ == '__main__':
    app.run(debug=True, port = 3000)