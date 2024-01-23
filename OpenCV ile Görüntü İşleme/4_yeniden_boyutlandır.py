import cv2

#
img = cv2.imread("lenna.png",1)  #0 ise siyah beyaz 1 ise renkli
print("Resim boyutu: " , img.shape) #"shape", bir dizi (array) veya matrisin boyutlarını, yani kaç satır ve sütundan oluştuğunu belirtir. 
cv2.imshow("Orijinal", img)
cv2.waitKey(0)

#Yeniden Boyutlandırma
imgResized = cv2.resize(img , (800,800)) #yukarıda okunmus resmi yeniden boyutlandırdık
print("Resized Img Shape", imgResized.shape)
cv2.imshow("Img Resized",imgResized)
cv2.waitKey(0)

#Kırpma
imgCropped = img[:200,:300] #OpenCv'de tam tersi önce yükseklik sonra genişliktir
cv2.imshow("Kirpilmis Resim",imgCropped)
cv2.waitKey(0)