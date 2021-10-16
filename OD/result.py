with open("./result_origin.txt", 'rb') as f :
    readLines = f.readlines()

import json
jsonList = []
for i, readLine in enumerate(readLines) :
    if (i + 1) % 3 == 0 :
        readLine = readLine
        print(readLine)
        readLineToJson = json.loads(readLine)
        print(type(readLineToJson))
        jsonList.append(readLineToJson)

saveImageClass = []
for jsonElement in jsonList :
    jsonElement = jsonElement["data"]
    jsonElementClass = []
    for jsonElementData in jsonElement :
        jsonElementClass.append(jsonElementData["class"])
    saveImageClass.append(jsonElementClass)

print(saveImageClass)