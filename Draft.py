import requests
import re
from bs4 import BeautifulSoup as BS

def getsynonyms(testWord):
    '''
    This Function take the string argument and then returns the synonyms of the
    string from www.thesaurus.com

    The returned value is a list of the synonyms
    '''
    r = requests.get("https://www.thesaurus.com/browse/"+ str(testWord).lower())

    want=BS(r.content, 'html.parser')
    tags=want.find_all(class_="css-1kg1yv8 eh475bn0")

    synonyms = []
    for things in tags:
        synonyms.append(re.sub("/browse/","",things['href']).strip())

    print(synonyms)
    return synonyms



testWord=['easy','medium','hard']
for things in testWord:
    getsynonyms(things)
