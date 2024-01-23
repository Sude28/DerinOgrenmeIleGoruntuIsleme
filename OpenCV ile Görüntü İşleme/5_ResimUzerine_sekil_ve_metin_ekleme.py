import cv2 
import numpy as np #resim yüklemek yerine numpy kütüphanesini kullanarak siyah bir resim oluşturucaz

#Resim Olustur
img = np.zeros((512,512,3) , np.uint8) #Bu kod satırı, np.zeros fonksiyonunu kullanarak, boyutları (512, 512, 3) olan bir dizi oluşturur. Bu dizi, 512 piksel yüksekliğe, 512 piksel genişliğe ve her bir pikselde 3 renk kanalına (kırmızı, yeşil, mavi) sahiptir   #`np.zeros` fonksiyonu, tüm pikselleri sıfırlar, yani siyah bir görüntü oluşturur.
print(img.shape)

cv2.imshow("Siyah",img)
cv2.waitKey(0)

#Cizgi Ekleme
cv2.line(img, (0,0), (512,512) ,(0,255,0),3) #(resim,başlangıç_noktası,bitiş_noktası,renk,kalınlık)  #renk->BGR(blue,green,red)
cv2.imshow("Cizgi",img)
cv2.waitKey(0)

#Dıkdortgen Ekleme
cv2.rectangle(img, (0,0),(256,256), (255,0,0), cv2.FILLED)  #(resim,başlangıç_noktası,bitiş_noktası,renk)   #cv2.FILLED doldurulmus demek
cv2.imshow("Dikdortgen",img)
cv2.waitKey(0)

#Cember Ekleme
cv2.circle(img,(300,300), 45 ,(0,0,255))  #(resim,merkez,yaricap,renk)  #cv2.FILLED eklersek daire olur
cv2.imshow("Cember",img)
cv2.waitKey(0)

#Metin Ekleme
cv2.putText(img, "Resim",(350,350),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))  #(resim,başlangıç noktası,font,yazı kalınlığı,renk)
cv2.imshow("Metin",img)
cv2.waitKey(0)