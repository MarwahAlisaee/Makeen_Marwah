import requests
from bs4 import BeautifulSoup

name = input("Enter article name: ")

URL = f"https://en.wikipedia.org/wiki/{name}"

html = requests.get(URL).text
soup = BeautifulSoup(html, 'html.parser')
content = soup.find(id='content')

title = content.find('h1').text.strip()
article = [p.text.strip() for p in content.find_all('p')]

print("title is", title)
print("article is", article)

