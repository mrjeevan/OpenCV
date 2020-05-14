import cv2
print("package_imported")
cv2.namedWindow("My_First_Output")
img = cv2.imread("Resources/grid.png")
cv2.imshow("My_First_Output", img)
cv2.waitKey(0)

v = cv2.VideoCapture(0) # ("Path Of Video") For video playback , if 0 webcam is used
v.set(3,500)
v.set(4,600)
v.set(10,0)
while True:
    success, img = v.read()
    cv2.imshow("Vedio_o/p", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
