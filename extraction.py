# OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV 
import numpy
import imutils
import argparse
import cv2
ans=1
 
# capture frames from a video
cap = cv2.VideoCapture('pedestriantraining.mp4')
pic_num = 1
pic_num2 = 1
if cap.isOpened():
    print "opened"
# loop runs if capturing has been initialized.
while True:
    # reads frames from a video
    ret, frames = cap.read()
    frameY, frameX, frameD = frames.shape
    img = cv2.resize(frames, (frameX/2, frameY/2))
    cv2.imshow('Resized', img)
    ans=input()
    if(ans==1):
        cv2.imwrite("neg/"+str(pic_num)+".jpg",img)
        pic_num += 1
    elif (ans==2):
        cv2.imwrite("pos/"+str(pic_num2)+".jpg",img)
        pic_num2 += 1
        # Wait for Esc key to stop
    if cv2.waitKey(33) == 27:
        break
 
# De-allocate any associated memory usage
cv2.destroyAllWindows()
