import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("yourname.jpg",0)
img=cv2.resize(img,(640,480))
img_equalization=cv2.equalizeHist(img)
cv2.imwrite("anh.png",img_equalization)
cv2.imshow("Anh goc",img)
cv2.imshow("Anh can bang hisogram",img_equalization)
hist1=cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist1,color='b')
hist2=cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist2,color='r')
plt.title('Image')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
