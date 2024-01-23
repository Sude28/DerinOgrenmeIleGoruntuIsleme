#Belirli renklerde bulunan nesnelerin tespitinin nasıl yapılacağını kontur bulma yöntemi ile öğreneceğiz.
#Konturlar basitçe aynı renk ve yoğunluğa sahip tüm sürekli noktaları birleştiren bir eğri olarak açıklanabilir.

#Kameradan gelen görüntüleri (RGB veya BGR) HSV'ye dönüştürücez. (HUE:Renkler, SATURATİON:Doygunluk, VALUE:Parlaklık)

import cv2
import numpy as np
from collections import deque #Tespit ettiğimiz objenin merkezini depolamak için kullanıcaz

buffer_size = 16
pts = deque(maxlen = buffer_size)
        