#Nesne tespiti:Amaç görüntü üzerinde bulunan nesnenin koordinatlarının genişlik ve yükseklik değerlerinin bulunmasıdır. Yani o nesnenin ne olduğu değil
#Nesneyi önce tespit ediyoruz sonra takip ediyoruz en son sınıflandırıyoruz

#Kenar algılama 'görüntü parlaklığının' keskin bir şekilde değiştiği noktaları tanımlamayı amaçlayan bir yöntemdir.

import cv2
import matplotlib.pyplot as plt
import numpy as np

#resmi içe aktar
img = cv2.imread("london.jpg",0) #0 değeri, görüntünün siyah-beyaz (grayscale) olarak okunmasını belirtir. 
plt.figure()
plt.imshow(img, cmap="gray") #cmap="gray": Görüntüyü siyah-beyaz (grayscale) olarak gösterir.
plt.axis("off")

edges = cv2.Canny(image= img, threshold1 =0 ,threshold2=255) #Herhangi bir threshold belirlemedik demek zaten resim 0 ile 255 arasında siyah-beyaz olduğu için
plt.figure()
plt.imshow(edges, cmap="gray") 
plt.axis("off")
#Herhangi bir threshold kullanmadığımız için bütün kenarlar ortaya çıktı. Nehirin kenarları yok ama onu da varmış gibi aldı

#Threshold değerlerini mantıklı şeyler seçelim.Medyan değeri genelde en iyi değerdir.
med_val = np.median(img)
print(med_val)

#alt ve üst threshold belirliyvez
low = int(max(0,(1-0.33)*med_val))
high = int(min(255,(1 + 0.33)*med_val))

print(low)
print(high)

edges = cv2.Canny(image= img, threshold1 =low ,threshold2=high) 
plt.figure()
plt.imshow(edges, cmap="gray") 
plt.axis("off")


#Tüm resme bluring uyguluyoruz detaylar biraz azalsın diye
blurred_img = cv2.blur(img, ksize=(5,5))
plt.figure()
plt.imshow(blurred_img, cmap="gray")
plt.axis("off")

med_val = np.median(blurred_img)
print(med_val)

low = int(max(0,(1-0.33)*med_val))
high = int(min(255,(1 + 0.33)*med_val))

print(low)
print(high)

edges = cv2.Canny(image= blurred_img, threshold1 =low ,threshold2=high) 
plt.figure()
plt.imshow(edges, cmap="gray") 
plt.axis("off")