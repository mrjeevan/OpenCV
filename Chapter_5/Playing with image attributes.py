import cv2
import numpy as np
from time import sleep
def empty(a):
    pass

img0 = cv2.imread("Resources/color.jpg")
img = cv2.resize(img0,(400,400))
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.namedWindow("Settings")
cv2.resizeWindow("Settings",600,270)
cv2.createTrackbar("Hue_Min","Settings",0,179,empty)
cv2.createTrackbar("Hue_Max","Settings",14,179,empty)
cv2.createTrackbar("Satu_Min","Settings",125,255,empty)
cv2.createTrackbar("Satu_Max","Settings",255,255,empty)
cv2.createTrackbar("Val_Min","Settings",213,255,empty)
cv2.createTrackbar("Val_Max","Settings",255,255,empty)

cv2.imshow("Normal",img)
cv2.imshow("HSV",imgHSV)
while True:

    Hue_Min = cv2.getTrackbarPos("Hue_Min","Settings")
    Hue_Max = cv2.getTrackbarPos("Hue_Max", "Settings")
    Satu_Min = cv2.getTrackbarPos("Satu_Min", "Settings")
    Satu_Max = cv2.getTrackbarPos("Satu_Max", "Settings")
    Val_Min = cv2.getTrackbarPos("Val_Min", "Settings")
    Val_Max = cv2.getTrackbarPos("Val_Max", "Settings")
    lower = np.array([Hue_Min,Satu_Min,Val_Min])
    upper = np.array([Hue_Max,Satu_Max,Val_Max])
    print(Hue_Max,Hue_Min,Satu_Max,Satu_Min,Val_Max,Val_Min)
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", imgResult)
    cv2.waitKey(3)
