import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("yourname.jpg")
img=cv2.resize(img,(640,480))
b,g,r=cv2.split(img)

#hiển thị từng kênh màu 
plt.hist(r.ravel(), 256, [0,256], color='r')
plt.hist(g.ravel(), 256, [0,256], color='g')
plt.hist(b.ravel(), 256, [0,256], color='b')
plt.xlabel('Intensity Value')
plt.ylabel('Pixel Count')

# Cân bằng histogram cho từng kênh màu
r_eq = cv2.equalizeHist(r)
g_eq = cv2.equalizeHist(g)
b_eq = cv2.equalizeHist(b)
# Ghép các kênh màu đã cân bằng thành ảnh RGB mới
img_eq1 = cv2.merge((r_eq, g_eq, b_eq))
img_eq2 = cv2.merge((b_eq, g_eq, r_eq))
img_eq3 = cv2.merge((g_eq, b_eq, r_eq))
# Hiển thị ảnh cân bằng histogram
cv2.imshow('Can bang1', img_eq1)
cv2.imshow('Can bang2', img_eq2)
cv2.imshow('Can bang3', img_eq3)
plt.show()
