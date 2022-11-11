import json

'''example output of list'''
# # test=[
#     'auto',
#     'automobile',
#     'bus',
#     'convertible',
#     'jeep',
#     'limousine',
#     'machine',
#     'motor',
#     'pickup',
#     'ride',
#     'station%20wagon',
#     'truck',
#     'van',
#     'wagon']


def writeToJSONFile(path,filename,data):
    filePathNameExt=path+filename 
    with open(filePathNameExt,'w') as fp:
        json.dump(data,fp)

def readFromJSONFile(path,filename):
    filePathNameExt=path+filename 
    with open(filePathNameExt,'r') as fp:
        return json.load(fp)

# path='./'
# filename='exampleWorking.json'

# data={}
# data['word']='jeep'
# data['synonms']=test
# # print(data)

# writeToJSONFile(path,filename,data)
# print(readFromJSONFile(path,filename))
    