import cv2
import time

#Video İsmi
video_name = "MOT17-04-DPM.mp4"

#Video İce Aktar : capture,cap
cap = cv2.VideoCapture(video_name) #Bu videoyu cap icerisine aktar

print("Genişlik:",cap.get(3))   # get fonksiyonunun 3. indeksini uygulayınca videonun genişliğini
print("Genişlik:",cap.get(4))   #4. indeksini uygulayınca videonun yüksekliğini elde ederiz

if cap.isOpened() == False:   #Video acilmiyorsa hata mesajı verdirdik
    print("Hata")
    
#Video Okuma    
while True:
    ret, frame =  cap.read()   #frame videonun icindeki her bir resim, ret(return) ise bu islemin basarili olup olmadıgı 

    if ret == True:
        time.sleep(0.01)  #kullanmazsak cok hizli akar
        cv2.imshow("Video",frame) #Yukarıda bir frame yani resimi okuyoruz burada da bu frame'i görselleştiriyoruz. Her frame için yapınca video oluyor bu nedenle while döngüsü 

    else:break #return edilecek şeyler varsa devam et bitince çık
    
    #Tüm videoyu izlemek istemezsek kendi isteğimizle çıkarsak
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()    #Video yakalamayı bırakıyoruz
cv2.destroyAllWindows()  #Tum pencereleri kapatıyoruz