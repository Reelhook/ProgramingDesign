import json

def readFromJSONFile(path,filename):
    filePathNameExt=path+filename 
    with open(filePathNameExt,'r') as fp:
        return json.load(fp)


def writeToJSONFile(path,filename,data):
    filePathNameExt=path+filename 
    # with open(filePathNameExt,'a') as fp:
    #     json.dump(data,fp)
    jsonData = json.dumps(data)
    with open(filePathNameExt,'a') as f:
        f.write(jsonData)
    




#  # load json module
# import json

# # python dictionary with key value pairs
# dict = {'Python' : '.py', 'C++' : '.cpp', 'Java' : '.java'}

# # create json object from dictionary
# json = json.dumps(dict)

# # open file for writing, "w" 
# f = open("dict.json","w")

# # write json object to file
# f.write(json)

# # close file
# f.close()   