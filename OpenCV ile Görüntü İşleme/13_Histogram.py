#Görüntü histogramı, dijital görüntüdeki ton dağılımının grafiksel bir temsili olarak işlev gören bir histogram türüdür.
#Her bir ton değeri için piksel sayısnı içerir.
#Belirli bir görüntü için histograma bakılarak, ton dağılımı anlaşılabilir.

import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("red_blue.jpg")
img_vis = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #normal haline çevirdik red green blue
plt.figure()
plt.imshow(img_vis)

print(img.shape)

img_hist = cv2.calcHist([img], channels=[0], mask = None, histSize = [256], ranges=[0,256]) #img_hist = cv2.calcHist([img], channels=[0], mask=None, histSize=[256], ranges=[0, 256]): Görüntünün histogramını hesaplar. channels=[0] görüntünün 0. (mavi) kanalındaki histogramı hesaplar. histSize=[256] histogramdaki bin sayısını belirtir. ranges=[0, 256] değer aralığını belirtir.
print(img_hist.shape)
plt.figure()
plt.plot(img_hist) #plt.plot(img_hist): Mavi kanalın histogramını çizdirir.

color = ("b","g","r")
plt.figure()
for i,c in enumerate(color):
    hist = cv2.calcHist([img], channels = [i], mask=None,histSize = [256], ranges=[0,256])
    plt.plot(hist, color=c) # #plt.plot(hist, color=c): Renk kanalının histogramını çizdirir. Döngü her bir renk kanalı için çalıştığı için mavi, yeşil ve kırmızı kanalların histogramları aynı grafik üzerinde çizilir.
    
    
#maskeleme işlemi kullanıcaz ve böylece resmin küçük bir bölümüne odaklanıcaz
golden_gate = cv2.imread("goldenGate.jpg")
golden_gate_vis = cv2.cvtColor(golden_gate, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(golden_gate_vis)

print(golden_gate.shape)

mask = np.zeros(golden_gate.shape[:2],np.uint8)   #golden_gate.shape[:2] ifadesi, golden_gate görüntüsünün yükseklik ve genişlik değerlerini döndürür. np.zeros() fonksiyonu, verilen boyutlarda ve veri tipinde (burada np.uint8 olarak belirtilmiş, 8-bit unsigned integer) sıfırlardan oluşan bir dizi oluşturur. Bu dizi, maskenin başlangıçta siyah (tüm pikseller değeri 0) olduğunu temsil eder.
plt.figure()
plt.imshow(mask,cmap="gray") #cmap="gray" ifadesi, görüntünün siyah-beyaz olarak gösterilmesini sağlar. Burada, maskenin piksellerinin değerleri 0 olduğu için siyah olacak ve beyaz arka plana sahip olacaktır

#Resim ile maskenin boyutları aynı bu nedenle maskeleme yaparsak simsiyah gözükücek bu nedenle maskede bir boşluk açıcaz.
mask[1500:2000,1000:2000] =255  #Bu aralığı alsın ve beyaz yapsın(255)
plt.figure()
plt.imshow(mask,cmap="gray")

masked_img_vis = cv2.bitwise_and(golden_gate_vis,golden_gate_vis,mask=mask) #cv2.bitwise_and() fonksiyonu, iki görüntü veya bir görüntü ile bir maske arasındaki bitwise AND işlemi (mantıksal VE işlemi) yapar. Bitwise AND işlemi, her iki görüntünün veya maskenin piksel değerlerini karşılaştırır ve yalnızca her iki piksel de beyaz (değer 1) olduğunda sonuç görüntüde beyaz bir piksel oluşturur. Diğer durumlarda, sonuç görüntüde siyah bir piksel oluşturulur (değer 0).
plt.figure()
plt.imshow(masked_img_vis,cmap="gray")
#Sonuç olarak, masked_img_vis değişkeni, golden_gate_vis görüntüsünün yalnızca maskenin beyaz piksellerine karşılık gelen bölgelerini içeren bir görüntüyü temsil eder

masked_img = cv2.bitwise_and(golden_gate,golden_gate,mask=mask) #Bu satırda, orijinal golden_gate görüntüsü, aynı görüntüyle (golden_gate) maskenin siyah-beyaz versiyonu (mask) ile filtrelenir. Bu işlem, maskeden etkilenen bölgeyi izole eder.
masked_img_hist = cv2.calcHist([golden_gate], channels=[0], mask = mask, histSize = [256], ranges=[0,256]) #masked_img_hist = cv2.calcHist([golden_gate], channels=[0], mask=None, histSize=[256], ranges=[0, 256]): Maskelenmiş görüntünün histogramını hesaplar. channels=[0] ifadesi, görüntünün 0. (mavi) kanalındaki histogramı hesaplar. histSize=[256] histogramdaki bin sayısını belirtir. ranges=[0, 256] değer aralığını belirtir.
plt.figure()
plt.plot(masked_img_hist) # Maskelenmiş görüntünün histogramını çizer


#Histogram Eşitleme :Kontrast(renkler arasındaki zıtlık,açıklık) arttırmayı sağlıyor.
img = cv2.imread("hist_equ.jpg",0)
plt.figure()
plt.imshow(img,cmap="gray")

img_hist = cv2.calcHist([img], channels=[0] ,mask = None, histSize = [256], ranges=[0,256])
plt.figure()
plt.plot(img_hist)

#esitleme
eq_hist = cv2.equalizeHist(img)
plt.figure()
plt.imshow(eq_hist,cmap="gray")

eq_img_hist = cv2.calcHist([eq_hist], channels=[0] ,mask = None, histSize = [256], ranges=[0,256])
plt.figure()
plt.plot(eq_img_hist)






