import json

def writeToJSONFile(path,filename,data):
    filePathNameExt=path+filename 
    with open(filePathNameExt,'a') as fp:
        json.dump(data,fp)

def readFromJSONFile(path,filename):
    filePathNameExt=path+filename 
    with open(filePathNameExt,'r') as fp:
        return json.load(fp)


    