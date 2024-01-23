#Görüntü gradyanı görüntüdeki yoğunluk veya renkteki yönlü bir değişikliktir.
#Kenar algılmada kullanılır.

import cv2
import matplotlib.pyplot as plt

#resmi içe aktar
img = cv2.imread("sudoku.jpg",0)
plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("Orijinal Img")

#x gradyan
sobelx = cv2.Sobel(img, ddepth = cv2.CV_16S,dx=1,dy=0, ksize=5)  #cv2.Sobel(): Bu fonksiyon, bir görüntü üzerinde Sobel kenar tespiti yapmak için kullanılır. ddepth = cv2.CV_16S: Bu argüman, işlem sırasında kullanılacak veri tipini belirtir. Sobel işlemi gradient değerleri hesaplar, bu nedenle bu değer tipi genellikle tamsayı olmalıdır. cv2.CV_16S tamsayı değeri kullanılır. dx=1 ve dy=0: Bu argümanlar, Sobel filtresinin x ve y yönündeki türevlerini belirtir. dx=1 x yönünde birinci dereceden türevi (x gradient) hesaplar, dy=0 ise y yönünde türevi hesaplamaz.ksize=5: Bu argüman, Sobel filtresinin kernel boyutunu belirtir. Sobel filtresi, gradient değerlerini hesaplamak için belirli bir piksel çevresindeki değerleri kullanır. Bu kernel boyutu, bu çevre piksellerin boyutunu belirtir. Genellikle tek sayılar kullanılır, çünkü kernel merkezinde bir piksel bulunmalıdır. Bu örnekte, 5x5 boyutunda bir kernel kullanılır.Bu kod satırı, görüntünün x yönündeki gradient değerlerini Sobel filtresi kullanarak hesaplar. Sonuç olarak, sobelx değişkeni, x yönündeki kenarları temsil eden bir görüntüyü içerir. Bu görüntüdeki yüksek değerler, görüntünün x yönündeki kenarlarını gösterir. Bu işlem, nesnelerin kenarlarını, kontürlerini veya diğer önemli özelliklerini tespit etmek için kullanılabilir.
plt.figure()
plt.imshow(sobelx, cmap="gray")
plt.axis("off")
plt.title("Sobelx Img")


#y gradyan
sobely = cv2.Sobel(img, ddepth = cv2.CV_16S,dx=0,dy=1, ksize=5)
plt.figure()
plt.imshow(sobely, cmap="gray")
plt.axis("off")
plt.title("Sobely Img")


#Laplacian gradyan
laplacian = cv2.Laplacian(img, ddepth=cv2.CV_16S)
plt.figure()
plt.imshow(laplacian, cmap="gray")
plt.axis("off")
plt.title("Laplacian Img")