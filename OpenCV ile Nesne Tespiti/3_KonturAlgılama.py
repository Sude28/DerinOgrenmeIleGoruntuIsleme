#Kontur analizi aynı renk ve yoğunluğa sahip tüm kesintisiz noktaları(sınırla birlikte) birleştirmeyi amaçlayan yöntemdir.
import cv2
import matplotlib.pyplot as plt
import numpy as np

#Resmi içe aktar
img = cv2.imread("contour.jpg",0)
plt.figure()
plt.imshow(img,cmap="gray")
plt.axis("off")

#Kontür analiz etme
contours, hierarch = cv2.findContours(img , cv2.RETR_CCOMP , cv2.CHAIN_APPROX_SIMPLE) #İkinci parametremiz hem iç hem de dış kontörü bulmak istediğini belirtiyor. Üçüncü parametremiz ise yatay dikey ve çapraz bölümleri sıkıştırmamızı sağlıyor ve yalnızca uç noktalarını bırakıyor.  

#Dış ve iç kpntürleri tutmak için bir matris oluşturucaz
external_contour = np.zeros(img.shape)  #np.zeros(img.shape) ifadesi, img görüntüsü ile aynı boyutta, tüm elemanları sıfır olan bir dizi oluşturur ve bu dizi external_contour değişkenine atanır.
internal_contour = np.zeros(img.shape)

for i in range(len(contours)):
    #external
    if hierarch[0][i][3] == -1:
        cv2.drawContours(external_contour, contours,i,255,-1) #Bu durumda, çizim rengi 255 (beyaz) olarak belirlenmiş (-1 değeri ile içi doldurulmuş), ve i indeksi ile belirtilen kontur çizilir
    #internal
    else:
        cv2.drawContours(internal_contour, contours,i,255,-1)
        
    #hierarch[0][i][0]: İçinde bulunduğu dış konturun indeksi.
    #hierarch[0][i][1]: Kendi içinde bulunan bir delik varsa, o deliğin indeksi. Yoksa, -1.
    #hierarch[0][i][2]: Kendi dışında bulunan bir iç kontur varsa, o iç konturun indeksi. Yoksa, -1.
    #hierarch[0][i][3]: Ebeveyn konturun indeksi. Eğer bir konturun dış kontur olup olmadığını belirlemek için kullanılır. Eğer dış kontur ise, bu değer -1 olur.    
    
plt.figure()
plt.imshow(external_contour,cmap="gray")
plt.axis("off")  

plt.figure()
plt.imshow(internal_contour,cmap="gray")
plt.axis("off")   