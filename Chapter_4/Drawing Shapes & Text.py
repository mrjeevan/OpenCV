import cv2
import numpy as np

img = np.zeros((500,500,3),np.uint8)
img[:] = (99,300,99)
cv2.line(img,(0,0),(500,500),(300,99,99),5) #(width,height)
cv2.rectangle(img,(10,10),(490,490),(99,99,255),3)
cv2.circle(img,(250,250),245,(99,255,255),3)
cv2.imshow("Created",img)
cv2.putText(img,"Hello world",(30,30),cv2.FONT_ITALIC,4,(120,200,9),2)
cv2.waitKey(0)
