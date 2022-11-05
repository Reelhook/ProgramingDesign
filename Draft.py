import requests
from bs4 import BeautifulSoup as BS

testWord="hard"

r = requests.get("https://www.thesaurus.com/browse"+ str(testWord).lower())

want=BS(r.content, 'html.parser')
if want.find(id="meanings"):
    print(want.find(id="meanings"))
# print(r.content)
# print(want)