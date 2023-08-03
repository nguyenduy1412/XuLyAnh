import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("yourname.jpg",1)
img=cv2.resize(img,(640,480))
hist=cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist,color='b')
plt.title('Image hisogram for')
color =('b','g','r')
for i,col in enumerate(color):
    histrgb=cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histrgb,color=col)
plt.show()