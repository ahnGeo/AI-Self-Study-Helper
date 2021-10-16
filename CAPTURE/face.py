import cv2
import time
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

cascade_fn = "haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(cascade_fn)

cam = cv2.VideoCapture(0)

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    face = cascade.detectMultiScale(img, 1.03, 5)
    
    if face is(): #no face in img
        ret, fram = cam.read()
        
        smtp = smtplib.SMTP('smtp.naver.com', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login('peacemiller@naver.com', 'dnflxordus')

        imageByte = cv2.imencode(".jpeg", fram)[1].tostring()
        msg = MIMEMultipart()
        imageMime = MIMEImage(imageByte)
        msg.attach(imageMime)
        
        msg['Subject'] = 'student is not studying'
        msg['From'] = 'peacemiller@naver.com'
        msg['To'] = 'peacemiller@naver.com'
        smtp.sendmail('peacemiller@naver.com', 'peacemiller@naver.com', msg.as_string())
            
        smtp.quit()
        
        print('done')
        break
    else:
        print(face)
    
    time.sleep(1)
    
