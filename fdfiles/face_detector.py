print("Starting facial detection task...")
import numpy as np
import cv2

# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv2.VideoCapture(1)
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for f in faces:
        print("found a face")
        continue

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
