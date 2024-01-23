import cv2

#capture
cap = cv2.VideoCapture(0)  #0 bilgisayardaki kameradır

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #Her frame'in genişliğini geitirir ve sonra int'e çevirir
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width,height)

#video kaydet
writer = cv2.VideoWriter("video_kaydi.mp4",cv2.VideoWriter_fourcc(*"DIVX"),20,(width,height))    #"video_kaydi.mp4":Videonun ismi   #cv2.VideoWriter_fourcc(*"DIVX"): Bu parametre, kullanılacak video codec'ini belirtir. DIVX codec'i, videoyu sıkıştırmak ve daha küçük bir dosya boyutu elde etmek için kullanılır. #20: Video dosyasının kare hızı 

while True:
    ret,frame = cap.read() #Frameleri okur
    cv2.imshow("Video",frame) #Okudugu frameleri ekranda gosterir
    
    writer.write(frame) #Frameleri kaydeder
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break  #q'ya basılınca çıkar

cap.release() #capture'yi serbest bırakıyoruz
writer.release() #writer'a yazma işlemi bitti diyoruz
cv2.destroyAllWindows() #Açık kalan pencere varsa kapatıyoruz