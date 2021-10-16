#################capture########################
import cv2
import os

cam = cv2.VideoCapture(0)
os.makedirs("./CamImages", exist_ok=True)
count = 0

#while문 안으로 procedure 집어넣기
while True:
    if count == 30 :
        break
    ret, img = cam.read()
    image = cv2.resize(image, (960, 540)) # 이미지 사이즈 960x540으로 변경 
    if(int(cam.get(1)) % 90 == 0): # 3초 하나씩 이미지 추출
        count += 1
        print('Saved frame number : ' + str(int(cam.get(1))))  
        cv2.imwrite("./CamImages/frame_%d.png" % count, image) # 추출된 이미지가 저장되는 경로  

###################capture#######################
###################OD_API########################
import urllib3
import json
import base64

openApiURL = "http://aiopen.etri.re.kr:8000/ObjectDetect"
accessKey = "c6b514be-f230-4b33-bdc0-7370e8a49d66"
imageFilePath_base = "./CamImages/frame_"
fileType = "png"

chosenContentsList = []
for idxForImages in range(1, count+1) :
    ImageFilePath = imageFilePath_base + idxForImages + '.' + fileType
    file = open(ImageFilePath, "rb")
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