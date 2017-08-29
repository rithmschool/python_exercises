from flask import Flask, render_template, request
import jinja2
import bs4
import urllib.request

app = Flask(__name__)

app.jinja_env.undefined = jinja2.StrictUndefined
app.jinja_env.auto_reload = True


@app.route('/')
def search():
    return render_template('form.html')

@app.route('/results')
def find_headline_by_keyword():
    url = "https://news.google.com"
    data = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(data, "html.parser")

    headlines = soup.select("span.titletext")
    anchors = soup.select("h2.esc-lead-article-title a")

    headlines_list = [headline.text for headline in headlines]
    anchors_list = [anchor["href"] for anchor in anchors]

    links = dict(zip(headlines_list, anchors_list))
    keyword = request.args.get('keyword')

    return render_template('news.html', links=links, keyword=keyword)

if __name__ == '__main__':
    app.run(debug=True)