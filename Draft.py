import requests
import re
from bs4 import BeautifulSoup as BS

testWord="easy"

r = requests.get("https://www.thesaurus.com/browse/"+ str(testWord).lower())

want=BS(r.content, 'html.parser')
tags=want.find_all(class_="css-1kg1yv8 eh475bn0")


synonyms = []
for things in tags:
    synonyms.append(re.sub("/browse/","",things['href']))

print(synonyms)



# print(r.content)
# print(want)