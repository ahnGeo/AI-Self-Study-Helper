# 영상의 의미지를 연속적으로 캡쳐할 수 있게 하는 class 
# # 영상이 있는 경로 

# vidcap = cv2.VideoCapture('./sample_video_1_cut.mp4') 

# count = 0 

# while(vidcap.isOpened()): 
#     ret, image = vidcap.read()  
#     # image = cv2.resize(image, (960, 540)) # 이미지 사이즈 960x540으로 변경 
#     if(int(vidcap.get(1)) % 60 == 0): # 30프레임당 하나씩 이미지 추출
#         print('Saved frame number : ' + str(int(vidcap.get(1))))  
#         cv2.imwrite("./Use60Frame/frame_%d.png" % count, image) # 추출된 이미지가 저장되는 경로  
#         count += 1 

# vidcap.release()

# 종료가 자동적으로 안 됨

#################capture########################
import cv2
import os

cam = cv2.VideoCapture(0)
os.makedirs("./CamImages", exist_ok=True)
count = 0

while True:
    if count == 30 :
        break
    ret, img = cam.read()
    image = cv2.resize(image, (960, 540)) # 이미지 사이즈 960x540으로 변경 
    if(int(cam.get(1)) % 60 == 0): # 30프레임당 하나씩 이미지 추출
        print('Saved frame number : ' + str(int(cam.get(1))))  
        cv2.imwrite("./CamImages/frame_%d.png" % count, image) # 추출된 이미지가 저장되는 경로  
        count += 1

###################capture#######################
###################OD_API########################

    
 