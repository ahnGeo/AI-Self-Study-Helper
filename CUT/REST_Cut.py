#-*- coding:utf-8 -*-
import urllib3
import json
import os

openApiURL = "http://aiopen.etri.re.kr:8000/VideoParse"
accessKey = "c6b514be-f230-4b33-bdc0-7370e8a49d66"
videoFilePath = "./sample_video_1_cut.mp4"

file = open(videoFilePath,'rb')
fileContent = file.read()
file.close();

requestJson = {
	"access_key": accessKey,
	"argument": {}
}

http = urllib3.PoolManager()
response = http.request(
	"POST",
	openApiURL,
	fields={
		'json': json.dumps(requestJson),
		'uploadfile': (os.path.basename(file.name), fileContent)
	}
)

print("[responseCode] " + str(response.status))
print("[responBody]")
responseData = response.data.decode('utf8').replace("'", '"')
responseData_json = json.loads(responseData)
responseData_str = json.dumps(responseData_json, indent=4)

with open("./result.txt", 'a') as f:
    f.write(responseData_str+'\n')


# openApiURL_Check = "http://aiopen.etri.re.kr:8000/VideoParse/status"
# responseData_Check = responseData_json["return_object"]["file_id"]

# requestJson_Check = {
# 	"access_key": accessKey,
# 	"argument": {
# 		# "file_id" : responseData_Check
# 		"file_id" : "f9faf1d20bc158f19410c4020272c19f.mp4"
# 	}
# }

# http = urllib3.PoolManager()
# response = http.request(
# 	"POST",
# 	openApiURL_Check,
# 	fields={
# 		'json': json.dumps(requestJson_Check),
# 	}
# )

# print("[responseCode] " + str(response.status))
# print("[responBody]")
# responseData = response.data.decode('utf8').replace("'", '"')
# responseData_json = json.loads(responseData)
# responseData_str = json.dumps(responseData_json, indent=4)

# with open("./result.txt", 'a') as f:
#     f.write(responseData_str+'\n')