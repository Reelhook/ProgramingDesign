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

def checkLocal(testWord):
    pass

def checkTimeStamp(testWord):
    pass

def write2Local(testWord,time,results):
    pass

'''
Things the results from below show be in a Dic() with the key being the word being
tested
'''
date=11072022
# testWord=['easy','medium','hard']
testWord=['gunner','butt','fuck','jeep','car','gun']
for word in testWord:
    checkLocal(word)
    checkTimeStamp(word)
    # getsynonyms(word.strip())
    write2Local(word, date, getsynonyms(word.strip()))
