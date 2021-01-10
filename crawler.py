import requests
from bs4 import BeautifulSoup

r = requests.get("https://hsreplay.net/battlegrounds/heroes/")

f = open("html.txt", "a")
f.write(r.text)
# soup = BeautifulSoup(r.text, 'html.parser')
# test = soup.find_all('div', {"class" , "bgs-table-cell__hero-right"})
# testt = [e.text for e in test]
# print(test)
f.close()