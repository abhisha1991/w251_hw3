print("Starting facial detection task...")
import numpy as np
import cv2
import time
import requests

# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv2.VideoCapture(1)
xml_file_url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
xml_file = "haarcascade_frontalface_default.xml"

r = requests.get(xml_file_url)
with open(xml_file, 'wb') as f:
    f.write(r.content)

face_cascade = cv2.CascadeClassifier(xml_file)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if frame is None:
        time.sleep(5)
        continue

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for f in faces:
        print("found a face")
        continue

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
