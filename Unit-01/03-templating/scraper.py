import bs4
import urllib

url = 'www.news.google.com'
data = urllib.urlrequest(url).read()
soup = bs4.BeautifulSoup(data.text, 'html.parse')

soup.find_all('td')
