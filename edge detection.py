import cv2
import numpy as np
import argparse
ans=0
th=10000
height=80
width=30

def leftlane():
        ans=0
        for a in range(height,height+width):
                for b in range(110,160):
                        ans=ans+edges[a][b]
                        edges[a][b]=255
        return ans

def midlane():
        ans=0
        for a in range(height,height+width):
                for b in range(370,420):
                        ans=ans+edges[a][b]
                        edges[a][b]=255
        return ans

def rightlane():
        ans=0
        for a in range(height,height+width):
                for b in range(650,700):
                        ans=ans+edges[a][b]
                        edges[a][b]=255
        return ans

def lane():
        ans=2
        l=leftlane()
        m=midlane()
        r=rightlane()
        if ((l<th)and(m<th)and(r<th)):
                ans=2
        elif ((l<th)and(m<th)and(r>th)):
                ans=3
        elif ((l<th)and(m>th)and(r<th)):
                ans=2
        elif ((l<th)and(m>th)and(r>th)):
                ans=2
        elif ((l>th)and(m<th)and(r<th)):
                ans=1
        elif ((l>th)and(m<th)and(r>th)):
                ans=2
        elif ((l>th)and(m>th)and(r<th)):
                ans=2
        elif ((l>th)and(m>th)and(r>th)):
                ans=2
        print l,m,r
        if (ans==1):
                print "left"
        elif (ans==2):
                print "middle"
        elif (ans==3):
                print "right"
        return 0

cam = cv2.VideoCapture('video2.mp4')
ret, img = cam.read()
#prev = img
#frameL, frameW, frameD = img.shape
#prev = cv2.resize(prev, (frameL/2, frameW/4))
#frameL, frameW, frameD = img.shape
#img = img[frameW/2:frameW, 0:frameL]
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#edgesOld = cv2.Canny(gray, 300, 320, apertureSize = 3)

while ret:
	ret, img = cam.read()
	if not ret:
		break;
	scaleDown = 4
#	frameL, frameW, frameD = img.shape
#	img = cv2.resize(img, (frameL/2, frameW/4))
	frameY, frameX, frameD = img.shape
#	img = img[0:100, 0:200]
	img = img[frameY/2:frameY*0.75, frameX*0.25:frameX]
	frameY, frameX, frameD = img.shape
	img = cv2.resize(img, (frameX/2, frameY/2))
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray,50, 100, apertureSize = 3)
	I,J=edges.shape
	I-I-1
	J=J-1
	lane()
#	print leftlane(),midlane(),rightlane()
#	img_diff = cv2.absdiff(edges, edgesOld)
	cv2.imshow('Resized', edges)
#	prev = img
	cv2.waitKey(10)

cv2.waitKey(0)
cam.release()
#cv2.destroyAllWindows()
