import cv2
import numpy as np

#Resmi İçe Aktarma
img = cv2.imread("lenna.png")
cv2.imshow("Orijinal",img)
cv2.waitKey(0)

#Yan yana birleştirme
hor = np.hstack((img,img))
cv2.imshow("Yatay",hor)
cv2.waitKey(0)

#Dikey birleştirme
ver = np.vstack((img,img))
cv2.imshow("Dikey",ver)
cv2.waitKey(0)
