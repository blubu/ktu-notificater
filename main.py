
import requests
from bs4 import BeautifulSoup

ktu = requests.get("https://www.ktu.edu.in/eu/core/announcements.htm")
soup = BeautifulSoup(ktu.text, 'html.parser')

with open('not.txt', 'r') as file:
    notes = file.readlines()

# soup.prettify()

note = soup.select("tr td ul li > b:first-child")
note = note[:10]

with open('not.txt', 'w') as file:
    for i in note:
        file.write(i.text+'\n')


