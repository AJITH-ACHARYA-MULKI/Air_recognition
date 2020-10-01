import cv2
import numpy as np
from bresenham import bresenham
cap=cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("cannot open webcam")
paintwindow=np.zeros((720,636,3))+255
cv2.namedWindow('paint',cv2.WINDOW_AUTOSIZE)
b_lower=np.array([100,60,60])
b_upper=np.array([140,255,255])
kernal=np.ones((5,5),np.uint8)
i=0
while True:
    ret ,frame=cap.read()
    frame=cv2.resize(frame,None ,fx=1.08,fy=1.5,interpolation=cv2.INTER_AREA)
    frame=cv2.flip(frame,1)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    blue_detect=cv2.inRange(hsv,b_lower,b_upper)
    blue_detect=cv2.erode(blue_detect,kernal,iterations=2)
    blue_detect=cv2.morphologyEx(blue_detect,cv2.MORPH_OPEN,kernal)
    blue_detect=cv2.dilate(blue_detect,kernal,iterations=1)
    (conto,_)=cv2.findContours(blue_detect.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if len(conto)>0:
        cnt=sorted(conto,key=cv2.contourArea,reverse=True)[0]
        ((x,y), radius)=cv2.minEnclosingCircle(cnt)
        cv2.circle(frame, (int(x), int(y)), int(radius), (0,255,255),2)
        moment=cv2.moments(cnt)
        center=(int(moment['m10'] / moment['m00']),int(moment['m01'] / moment['m00']))
        c3,c4=center
        if i==1:
            points=np.array(list(bresenham(c1,c2,c3,c4)), np.int32)
            points=points.reshape((-1,1,2))
            cv2.polylines(paintwindow,points,True,(0,255,0),2)
        c1,c2=center
        i=1
    else:
        i=0
    cv2.imshow('Input',frame)
    cv2.imshow('paint',paintwindow)
    #cv2.imshow('hsv',blue_detect)
    c=cv2.waitKey(1)
    if c==27:
        break
cap.release()
cv2.destroyAllWindows()
    
