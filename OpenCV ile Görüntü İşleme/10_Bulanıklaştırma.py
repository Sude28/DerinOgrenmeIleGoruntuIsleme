#Ortalama Bulanıklaştırma
#Çekirdek alanı altındaki tüm piksellerin ortalamasını alır ve bu ortalamayı merkezi öğe ile yer değiştirir.

#Gauss Bulanıklaştırma
#Ortalama Bulanıklaştırma'daki kutular yerine Gauss çekirdeği kullanılır.SigmaX ve sigmaY, X ve Y yönlerindeki standart sapmayı belirtmeliyiz.

#Medyan Bulanıklaştırma
#Çekirdek alanı altındaki tüm piksellerin medyanını alır ve merkezi öğe bu medyan değerle değiştirilir.

import cv2
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore") #Uyarıları kaldırdık

#bluring(detayı azaltır,gürültüyü engeller)
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img) #Matplotlib figüründe belirtilen görüntüyü çizer, ancak ekranda görüntüyü göstermez.
plt.axis("off")
plt.title("orijinal")
plt.show() # figürdeki tüm içeriği ekranda gösterir

"""
Ortalama Bulanıklaştırma Yöntemi
"""
dst2 = cv2.blur(img, ksize=(3,3)) #kutucuğun boyutu 3'e 3
plt.figure()
plt.imshow(dst2)
plt.axis("off")
plt.title("Ortalama Blur")
plt.show()


"""
Gauss Bulanıklaştırma Yöntemi
"""
gb = cv2.GaussianBlur(img, ksize=(3,3), sigmaX=7)   #sigmaX=7: Bu parametre, Gauss filtresinin standart sapmasını belirtir. Standart sapma, Gauss filtresinin dağılımının genişliğini kontrol eder. Daha büyük bir standart sapma, filtre daha fazla yayılacaktır. Burada, sigmaX değeri 7 olarak ayarlanmıştır,
plt.figure()
plt.imshow(gb)
plt.axis("off")
plt.title("Gauss Blur")
plt.show()

"""
Medyan Bulanıklaştırma Yöntemi
"""
mb = cv2.medianBlur(img, ksize=3)  #ksize=3: Bu parametre, median filtresinin boyutunu belirtir. Median filtresi, belirtilen boyut içindeki piksellerin medyan değerini hesaplar. Burada, ksize=3 olduğu için 3x3 boyutunda bir median filtresi kullanılır. Bu, her pikselin değerini kendisi ve çevresindeki 8 pikselin medyan değeriyle değiştirir.
plt.figure()
plt.imshow(mb)
plt.axis("off")
plt.title("Medyan Blur")
plt.show()
 

#Noise'a ihityacımız var, resimlerin üzerine noise(gürültü yani bozuk resim yapıyoruz nasıl düzelteceğimizi görebilmek için) koyalım ki kullandığımız bulanıklaştırma yöntemlerinin işe yaradığını görelim.

def gaussianNoise(image):
    row ,col , ch = image.shape #image.shape satır sütun ve renk sayısı(RGB)'nı return eder
    mean = 0
    var = 0.05
    sigma = var**0.5
    
    gauss = np.random.normal(mean,sigma,(row,col,ch)) #belirtilen ortalamaya (mean) ve standart sapmaya (sigma) sahip Gaussian gürültü oluşturulur.
    gauss = gauss.reshape(row,col,ch) 
    noisy = image + gauss
    
    return noisy

#Ice aktar ve normalize et(0 ile 255 arasında degisen degerleri 0 ile 1 arasına taşımak) Cunku gaussianNoise piksel degeri 0 ile 1 arasında bizim orijinal resim 0 ile 255 arasında
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255
plt.figure()
plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("Orijinal")
plt.show()

gaussianNoisyImage = gaussianNoise(img)
plt.figure()
plt.figure()
plt.imshow(gaussianNoisyImage)
plt.axis("off")
plt.title("Gauss Noisy")
plt.show()

#gauss blur
gb2 = cv2.GaussianBlur(gaussianNoisyImage, ksize=(3,3), sigmaX=7)   #sigmaX=7: Bu parametre, Gauss filtresinin standart sapmasını belirtir. Standart sapma, Gauss filtresinin dağılımının genişliğini kontrol eder. Daha büyük bir standart sapma, filtre daha fazla yayılacaktır. Burada, sigmaX değeri 7 olarak ayarlanmıştır,
plt.figure()
plt.imshow(gb2)
plt.axis("off")
plt.title("with Gauss Blur")
plt.show()
#daha az gürültü ama detaylar da azalıyor


#Tuz ve karabiber gibi siyah ve beyaz noktacıklar ekliycez resmimize sanki öyle bozuk bir resimmiş gibi sonra da medyanblur ile düzelticez
def saltPepperNoise(image):
    
    row, col, ch = image.shape
    s_vs_p = 0.5
    
    amount = 0.004
    
    noisy = np.copy(image)
    
    # salt beyaz
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy[coords] = 1
    
    # pepper siyah
    num_pepper = np.ceil(amount * image.size * (1 - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy[coords] = 0
    
    return noisy
       
spImage = saltPepperNoise(img)   
plt.figure(), plt.imshow(spImage), plt.axis("off"), plt.title("SP Image")

mb2 = cv2.medianBlur(spImage.astype(np.float32), ksize = 3)
plt.figure(), plt.imshow(mb2), plt.axis("off"), plt.title("with Medyan Blur")


