import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("img1.JPG")
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB) #opencv'de renkler rgb değil bgr bu nedenle biz de dönüştürüyoruz.
img2 = cv2.imread("img2.JPG")
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)


#Matplotlib'te bir figür (figure) oluşturmanın ana sebeplerinden biri, birden fazla alt grafik (subplot) içerebilen bir çizim alanı yaratmaktır.Bu şekilde, birden fazla grafik veya görüntüyü aynı figür içinde düzenleyebilir ve karşılaştırabilirsiniz.
plt.figure() #Bu ifade, yeni bir figür (çizim) oluşturur
plt.imshow(img1) #Matplotlib kütüphanesini kullanarak bir görüntüyü görselleştirmek için kullanılır. Verilen bir görüntüyü ekranda gösterir. 

plt.figure()
plt.imshow(img2)

#Aynı boyutta olmalılar
print(img1.shape)
print(img2.shape) #Farklı boyuttalarmış bu nedenle ikisini de aynı boyutta yapıyoruz.
img1=cv2.resize(img1,(600,600))
img2=cv2.resize(img2,(600,600))

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

#Karıştırılmış resim = alpha_katsayısı*img1 + beta_katsayısı*img2
blended = cv2.addWeighted(src1 = img1, alpha=0.6, src2 = img2, beta=0.6, gamma = 0) #İkisinden de 0.6 
plt.figure()
plt.imshow(blended)
