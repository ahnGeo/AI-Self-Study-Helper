
#-*- coding:utf-8 -*-
import urllib3
import json
import base64

openApiURL = "http://aiopen.etri.re.kr:8000/ObjectDetect"
accessKey = "c6b514be-f230-4b33-bdc0-7370e8a49d66"
chosenFileList = ['44', '95', '98', '100', '102', '116', '132', '136']
imageFilePath = "./frame_for_video_1/chosen/frame_"
fileType = "png"

chosenContentsList = []
for elementForChosenFileList in chosenFileList :
    chosenImageFilePath = imageFilePath + elementForChosenFileList + '.' + fileType
    file = open(chosenImageFilePath, "rb")
    imageContents = base64.b64encode(file.read()).decode("utf8")
    chosenContentsList.append(imageContents)
    file.close()

requestJsonList = []
for chosenContents in chosenContentsList :
    requestJson = {
        "access_key": accessKey,
        "argument": {
            "type": fileType,
            "file": chosenContents
        }
    }
    requestJsonList.append(requestJson)
 
http = urllib3.PoolManager()
for requestJson in requestJsonList :
    response = http.request(
        "POST",
        openApiURL,
        headers={"Content-Type": "application/json; charset=UTF-8"},
        body=json.dumps(requestJson)
    )

    print("[responseCode] " + str(response.status))
    print("[responBody]")
    print(type(response.data))
    responseData = response.data.decode('utf8').replace("'", '"')
    responseData = json.loads(responseData)
    print(type(responseData))
    responseData = json.dumps(responseData, indent=4)
    print(response.data)

    with open("./result.txt", 'a') as f:
       f.write(responseData+'\n')