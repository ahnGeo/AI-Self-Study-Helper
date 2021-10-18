#################capture########################
import cv2
import os
import urllib3
import json
import base64
from tkinter import *
import tkinter.messagebox


cam = cv2.VideoCapture(0)
os.makedirs("./CamImages", exist_ok=True)
count = 0

while True:
    if count == 10 :
        break
    ret, image = cam.read()
    image = cv2.resize(image, (960, 540)) 
    if(int(cam.get(1)) % 90 == 0): # 3초 하나씩 이미지 추출
        count += 1
        print('Saved frame number : ' + str(int(cam.get(1))))  
        cv2.imwrite("./CamImages/frame_%d.png" % count, image) # 추출된 이미지가 저장되는 경로  

###################capture#######################
###################OD_API########################
        openApiURL = "http://aiopen.etri.re.kr:8000/ObjectDetect"
        accessKey = "c6b514be-f230-4b33-bdc0-7370e8a49d66"
        fileType = "png"
        imageFilePath = "./CamImages/frame_" + str(count) + "." + fileType

        file = open(imageFilePath, "rb")
        imageContents = base64.b64encode(file.read()).decode("utf8")
        file.close()

        requestJson = {
            "access_key": accessKey,
            "argument": {
                "type": fileType,
                "file": imageContents
            }
        }
        
        http = urllib3.PoolManager()
        # for requestJson in requestJsonList :
        response = http.request(
            "POST",
            openApiURL,
            headers={"Content-Type": "application/json; charset=UTF-8"},
            body=json.dumps(requestJson)
        )

        print("[responseCode] " + str(response.status))
        print("[responBody]")
        responseData = response.data.decode('utf8').replace("'", '"')
        responseData = json.loads(responseData)
        print(responseData)
        
        # with open("./result.txt", 'a') as f:
        #    f.write(responseData+'\n')

###################OD_API########################
###################Check studying state##########
        if responseData["return_object"] == {} :
            jsonListInFrame = []
        else :
            jsonListInFrame = responseData["return_object"]["data"]
            classesInFrame = []
            for jsonInFrame in jsonListInFrame :
                classesInFrame.append(jsonInFrame["class"])
        
        if "cell phone" in classesInFrame or "person" not in classesInFrame or jsonListInFrame == []:
            #alert
            window = Tk()
            window.title("Alert")
            tkinter.messagebox.showwarning("Alert", "Hey! Do your job")





































