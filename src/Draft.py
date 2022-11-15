import requests
import re
import time
import MyJSONReadWrite as myJS
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

    # print(synonyms)
    return synonyms

def checkTimeStamp(testWord):
    pass


'''
Things the results from below show be in a Dic() with the key being the word being
tested
'''



testWord=['cat','dog']
# testWord=['gunner','butt','fuck','jeep','car','gun']
path='./'
filename='testMultipeDic.json'

myDics=[]
for word in testWord:
    data={}
    data['word']= word
    data['synonms']= getsynonyms(word.strip())
    myJS.writeToJSONFile(path,filename,data)
    

print(myJS.readFromJSONFile(path,filename))



