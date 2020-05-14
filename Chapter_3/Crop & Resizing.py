import cv2

img = cv2.imread("Resources/grid.png")
print(img.shape) # (Height,Width,bgr)
imgResize = cv2.resize(img,(400,300)) # (src,(Width,Height))
imgResize2 = cv2.resize(img,(722,577)) # (Width , Height)
cv2.imshow("Normal",img)
cv2.imshow("Res",imgResize)
cv2.imshow("Res_2",imgResize2)

imgCrop = img[10:600,10:500]  # [height_min:height_max,width_min:width_max]

cv2.imshow("Croped",imgCrop)
cv2.waitKey(0)
