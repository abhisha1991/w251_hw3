print("Starting facial detection task...")
import numpy as np
import cv2
import time
import requests
import random
import os

# create temp directory for images
path = os.getcwd() + "/img"
try:
    os.makedirs(path, exist_ok = True)
except e:
    print("Could not create image directory")
    raise e

# download the xml file for the model
xml_file_url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
xml_file = "haarcascade_frontalface_default.xml"
r = requests.get(xml_file_url)
with open(xml_file, 'wb') as f:
    f.write(r.content)

# set up classifier
face_cascade = cv2.CascadeClassifier(xml_file)

# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv2.VideoCapture(1)

while(True):
    time.sleep(10)
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame not captured, sleep 5 seconds
    if ret is False:
        time.sleep(5)
        continue

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for f in faces:
        # bad design, needs to be revisited
        img_name = "{0}/testimage.jpg".format(path)
        cv2.imwrite(img_name, frame)
        image = cv2.imread(img_name)
        # finally send the image via mqtt


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
