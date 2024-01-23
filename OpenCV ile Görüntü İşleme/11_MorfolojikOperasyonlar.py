#Morfolojik Operasyonlar: Erozyon,genişleme,açma,kapatma ve morfolojik gradyan
#Erozyon: Temel fikir toprak erozyonu gibidir. Ön plandaki nesnenin sınırlarını aşındırır
#Genişleme: Erozyonun tam tersidir. Ön plandaki  nesnenin sınırları artar.
#Açma: Erozyon+Genişleme'dir. Gürültünün giderilmesinde faydalıdır.
#Kapama: Açmanın tersidir. Genişleme + erozyon'dur. Ön plamdaki nesnelerin içindeki küçük delikleri veya nesne üzerindeki küçük siyah noktaları kapatmak için kullanışlıdır.
#Morfolojik Gradyan : Bir görüntünün genişlemesi ve erozyonu arasındaki farktır.Nesnenin ortasında boşluklar meydana gelir.
import cv2
import matplotlib.pyplot as plt
import numpy as np

#resmi içe aktar
img = cv2.imread("datai_team.jpg",0)
plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("Orijinal")

#Erozyon
kernel = np.ones((5,5),dtype = np.uint8) #dtype=np.unit8 yani int yapıyoruz
result = cv2.erode(img , kernel,iterations=1)  #iteration=1:kaç kere iterasyon yapıyım
plt.figure()
plt.imshow(result, cmap="gray")
plt.axis("off")
plt.title("Erozyon")

#Genişleme
result2 = cv2.dilate(img, kernel, iterations=1)
plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("Genişleme")

#Açılmayı beyaz gürültüyü(white noise) azaltmak için yaparız. Bu nednele ilk önce beyaz gürültü oluşturacağız.
whiteNoise = np.random.randint(0,2,size=img.shape[:2])  #np.random.randint() fonksiyonu kullanılarak 0 (dahil) ile 2 (hariç) arasında rastgele tamsayılar üretilir. size=img.shape[:2] ifadesi, img adlı bir görüntünün (veya resmin) boyutlarına uygun bir matris oluşturulmasını sağlar. Bu matris, beyaz gürültüyü temsil eder.
whiteNoise = whiteNoise*255  #Üretilen rastgele tamsayılar 0 ile 255 arasına ölçeklenir. Böylece, bu değerler siyah-beyaz bir görüntünün piksel değerlerine uygun hale getirilir.
plt.figure()
plt.imshow(whiteNoise, cmap="gray")
plt.axis("off")
plt.title("White Noise")

noise_img = whiteNoise + img
plt.figure()
plt.imshow(noise_img, cmap="gray")
plt.axis("off")
plt.title("White Noise")

#Açılma
opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN, kernel)
plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("Acilma")


#Kapanmayı yapabilmek için black noise'a ihtiyacımız var
blackNoise = np.random.randint(0,2,size=img.shape[:2])  
blackNoise = whiteNoise*-255 
plt.figure()
plt.imshow(blackNoise, cmap="gray")
plt.axis("off")
plt.title("Black Noise")

black_noise_img = blackNoise + img
black_noise_img[black_noise_img <= -245] = 0  #Black noise'umuz white noise'a benxediği için filtreleme yaptık
plt.figure()
plt.imshow(black_noise_img, cmap="gray")
plt.axis("off")
plt.title("Black Noise Img")

#Kapatma
closing= cv2.morphologyEx(black_noise_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)
plt.figure()
plt.imshow(opening, cmap="gray")
plt.axis("off")
plt.title("Kapama")


#Gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.figure()
plt.imshow(gradient, cmap="gray")
plt.axis("off")
plt.title("Gradyan")








