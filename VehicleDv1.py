#! /usr/bin/python
 
import cv2
 
face_cascade = cv2.CascadeClassifier('ped.xml')
vc = cv2.VideoCapture('1.mp4')
 
if vc.isOpened():
    rval , frame = vc.read()
else:
    rval = False
c1=500
area=0
pos=0
r1=0
center=500
while True:
    rval, frame = vc.read()
    frameY, frameX, frameD = frame.shape
    frame = cv2.resize(frame, (frameX/4, frameY/4))
 #   frame = frame[c1:c1+500,r1+700:r1+1700]
    # car detection.
    #cars = face_cascade.detectMultiScale(frame, 1.7, 1)
    cars = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=2,minSize=(26, 74),
                                        maxSize=(70, 174))
    ncars = 0
    for (x,y,w,h) in cars:
        area=w*h
        pos=x+(h/2)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        ncars = ncars + 1
        #print area
        if(pos>center):
            print "right"
        else:
            print "left"
    # show result
    cv2.imshow("Result",frame)
    #print ncars
    cv2.waitKey(1)
vc.release()
