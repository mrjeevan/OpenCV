'''
* uses camera to capture image
press q to capture images

1st image with object and background
2nd image only background

vary 'th' to improve results 
'''


import cv2
print("package_imported")
import numpy as np



v = cv2.VideoCapture(0) # ("Path Of Video") For video playback
v.set(3,300)
v.set(4,750)
v.set(10,0)
i = 1
while i:
    aimg = []
    aimg2 = []
    while True:
        success, img = v.read()
        aimg = np.array(img)
        cv2.imshow("img 1", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # v.release()
            break

    while True:
        success, img2 = v.read()
        aimg2 = np.array(img2)
        cv2.imshow("img 2", img2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # v.release()
            break

    appen = np.zeros_like(aimg2)
    i = 0
    th = 25
    while i < len(aimg):
        k = aimg[i]

        for j in range(len(k)):

            if (aimg2[i][j][0] - th < aimg[i][j][0] < aimg2[i][j][0] + th) and (
                    aimg2[i][j][0] - th < aimg[i][j][1] < aimg2[i][j][1] + th) and (
                    aimg2[i][j][0] - th < aimg[i][j][1] < aimg2[i][j][2] +th):
                appen[i][j] = [0, 0, 0]

            else:
                appen[i][j] = aimg[i][j]
        i += 1
        cv2.imshow("Made", appen)
        cv2.waitKey(1)

    i = 0
cv2.imshow('Final', appen)
cv2.waitKey(0)
v.release()
cv2.destroyAllWindows()
