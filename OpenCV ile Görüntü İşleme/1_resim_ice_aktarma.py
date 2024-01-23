import cv2 #opencv kütüphanesini import ettik

#Ice Aktarma
img = cv2.imread("vangogh-starynight.jpg", 0) #0'ın anlamı siyah ve beyazlardan oluşan resim demek

#Gorsellestirme(Opencv kutuphanesi ile)
cv2.imshow("Ilk Resim", img)
k = cv2.waitKey(0) & 0xFF #genellikle bu kod, bir pencere gösterildiğinde pencerenin açık kalmasını sağlamak ve kullanıcının pencereyi görüntüledikten sonra kapatmak için bir tuşa basmasını beklemek için kullanılı

if k == 27:      
    cv2.destroyAllWindows()
elif k ==  ord('s'):
    cv2.imwrite("vangogh-starynight-gray.jpg",img)
    cv2.destroyAllWindows()

