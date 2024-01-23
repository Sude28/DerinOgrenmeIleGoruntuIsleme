import cv2
import matplotlib.pyplot as plt

#resmi içe aktar
img = cv2.imread("img1.JPG")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")  #Eksenleri kapattık
plt.show()

#esikleme
_, thresh_img = cv2.threshold(img, thresh=60, maxval=255, type=cv2.THRESH_BINARY)           # thresh=60 üzerindeki yerleri görmek istemiyoruz onları beyaz yapıcaz maxval sınır 0 ile 255 arasında.   THRESH_BINARY, 60 ile 255 arasını beyaz yapıyor

#cv2.threshold() Fonksiyonu: Bu fonksiyon, bir görüntüyü belli bir eşik değeri (threshold) kullanarak ikili (siyah-beyaz) hale dönüştürür. Bu ikili görüntüde, eşik değerini aşan pikseller beyaz yapılır, eşik değerini geçemeyen pikseller ise siyah yapılır.
#thresh: Eşik değeri. Bu değeri geçen pikseller beyaz yapılır, geçemeyenler siyah yapılır.
#maxval: Eşik değerini geçen piksellerin alacağı maksimum değer. Burada 255 olarak belirlenmiş, yani geçen pikseller beyaz olarak ayarlanır.

plt.figure()
plt.imshow(thresh_img,cmap="gray")
plt.axis("off")
plt.show()

#therasold uygulayınca bu resim için konuşuyoruz dağların sol kısmı kayboldu sağ kısmı daha da belirginleşti yani böyle olunca bütünü bozduk.Bu bütünü bozmamak için adapting therasholding kullanıcaz

#Uyarlamalı Eşikleme :Algoritma görünütünün herhangi bölgeleri için eşiği hesaplıyor böylece her bölgeye göre threshold değişiyor;
thresh_img2 = cv2.adaptiveThreshold(img ,255 , cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY, 11, 8)
#cv2.ADAPTIVE_THRESH_MEAN_C: Adaptif eşikleme yöntemi olarak lokal ortalama (mean) değeri kullanılır.
#cv2.THRESH_BINARY: Eşik değerini geçen pikseller beyaz, geçemeyenler siyah yapılır.
#11: Eşik hesaplanırken kullanılacak blok boyutu. Bu değer, adaptif eşikleme için kullanılacak piksellerin lokal ortalamasını hesaplamak için kullanılacak komşu piksel sayısını belirtir.
#8: Lokal ortalama hesaplanırken eşik değeri üzerine eklenen veya çıkarılan bir değer. Bu, hesaplanan lokal ortalama değerine eklenir veya çıkarılır.
plt.figure()
plt.imshow(thresh_img2,cmap="gray")
plt.axis("off")
plt.show()