import cv2
import numpy as np

#resmi içe aktarma
img = cv2.imread("kart.png")
cv2.imshow("Orijinal",img)
cv2.waitKey(0)

width = 400 
height = 500

#point1:şimdiki koordinatları  point2:olmasını istediğimiz koordinatlar
pts1 = np.float32([[230,1],[1,472],[540,150],[338,617]])  #Numpy kütüphanesinin 'np.float32' veri türünü kullanarak dört adet 2-boyutlu noktayı içeren bir Numpy dizisi 
pts2 = np.float32([[0,0],[0,height],[width,0],[width,height]])

#transformu gerçekleştirebilmek için perspektif transform matrisini elde etmemiz gerekiyor
matrix = cv2.getPerspectiveTransform(pts1,pts2)
print(matrix)

#Çevirme işlemini gerçekleştiricez
imgOutput = cv2.warpPerspective(img, matrix, (width,height)) #Orijinal görüntüyü perspektif dönüşüm matrisi kullanarak yeni boyutlara uygun şekilde dönüştürür.
cv2.imshow("NihaiResim",imgOutput)
cv2.waitKey(0)