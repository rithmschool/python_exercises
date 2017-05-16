# Use BeautifulSoup to go to https://news.google.com
# and print out all of the headlines on the page

import bs4
import urllib.request

url = "https://news.google.com"
data = urllib.request.urlopen(url).read()
soup = bs4.BeautifulSoup(data, "html.parser")

# span class="titletext" or span.titletext

headlines = soup.select("span.titletext")

# titles = [headline.text for headline in headlines]
# print(titles)

headlines = soup.select("span.titletext")
anchors = soup.select("h2.esc-lead-article-title a")
# print(anchors)

headlines_list = [headline.text for headline in headlines]
anchors_list = [anchor['href'] for anchor in anchors]
# print(anchors_list)

links = dict(zip(headlines_list, anchors_list))
print(links)

# Write a function called find_headline_by_keyword
# that lets you search those headlines for keywords
# and returns a list of all headlines that match
# all keywords provided

# def find_headline_by_keyword(keyword):
# 	return [link for link in links if keyword in links]

# print(find_headline_by_keyword("Trump"))