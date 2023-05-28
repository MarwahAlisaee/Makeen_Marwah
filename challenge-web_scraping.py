import requests
from bs4 import BeautifulSoup
import json

country =input("Enter country name: ")
code = input("Enter code country name: ")

URL ="https://www.wunderground.com/weather/"+code+"/"+country
# HTTP request

html = requests.get(URL).content
soup = BeautifulSoup(html, 'html.parser')

temp = soup.find('span', attrs={'class': 'wu-value wu-value-to'}).text
Clouds = soup.find('span', attrs={'class':  'wx-value'}).text
humidity = soup.find('span', attrs={'class':  'test-false wu-unit wu-unit-humidity ng-star-inserted'}).text
pressure = soup.find('span', attrs={'class':  'test-false wu-unit wu-unit-pressure ng-star-inserted'}).text

# printing all the data
h=((int(temp)-32)*5)/9  
print("Temperature is", h)
print("Humidity is", humidity)
print("Clouds", Clouds)
print("pressure is", pressure)


