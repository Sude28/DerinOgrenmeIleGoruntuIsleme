#Bilgisayarla görmede genellikle bir resmin/videonun farklı çerçeveleri arasında eşleşem noktalar bulmamız gerekir. Çünkü iki görüntünün birbiryle nasıl ilişkili olduğunu bilirsek her iki görüntüyü de bilgi almak için kullanabiliriz.Bu eşleşen noktalar da kenarlar ve köşelerdir.
#KÖSE_ALGILAMA:Köşeler iki kenarın kesişimi olduğu için bu iki kenarın yönlerinin değiştiği bir noktayı temsil eder. 
  #Köşeler resimdeki renk geçişindeki bir varyasyonu temsil ettiğinden bu "varyasyonu" arayacağız. Görüntü yoğunluğundaki varyasyonu arayacağız.
  
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("sudoku.jpg",0)
img = np.float32(img)  
print(img.shape)
plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")

#Harris corner detection
dst = cv2.cornerHarris(img, blockSize=2, ksize=3, k=0.04)  #blocksize komşuluk boyutu (ne kadar komşusuna bakacağımızı belirliyor) ,ksize kutucuğun boyutu, Daha büyük bir k değeri, daha az hassas köşeler üretirken, daha küçük bir k değeri daha hassas köşeler üretir.
plt.figure()
plt.imshow(dst, cmap="gray")
plt.axis("off")

dst = cv2.dilate(dst,None)
img[dst>0.2*dst.max()] = 1 #dst değişkenini bir genişleme işlemine tabi tutar. Genişleme işlemi, dst matrisinin her bir öğesini, matrisin orijinal değerinin 0.2 katından daha büyükse 1 olarak ayarlar. Bu, köşeleri daha belirgin hale getirir.
plt.figure()
plt.imshow(dst, cmap="gray")
plt.axis("off")

#shi tomsai detection
img = cv2.imread("sudoku.jpg",0)
img = np.float32(img) 
corners = cv2.goodFeaturesToTrack(img, 120, 0.01, 10)  #Görüntüdeki en iyi 100 köşeyi bulmaya çalışır. Bu, Shi-Tomasi köşe algılama yöntemini kullanarak yapılır. İkinci parametre, tespit edilen köşe sayısını temsil eder. Üçüncü parametre, köşelerin kalitesini belirler. Dördüncü parametre, minimum euclidean uzaklığıdır; yani, tespit edilen köşeler arasındaki minimum mesafe.
corners = np.int64(corners)
#7'nin köşesini de köşe saydığı için 100 tane değil 120 tane köşe vardır diycez.

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,(125,125,125),cv2.FILLED)
    #Her bir köşe noktasını alır, ve bu noktaları görüntüde dairelerle işaretler. Bu, cv2.circle() fonksiyonu ile yapılır. Dairelerin merkezi, köşenin koordinatlarıdır ve yarıçapı 3 pikseldir. Dairelerin rengi (125, 125, 125) olarak belirlenmiştir ve içini doldurmak için cv2.FILLED kullanılır.
plt.imshow(img)
plt.axis("off")   