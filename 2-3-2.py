import cv2
import numpy as np
img=cv2.imread('anh.png')
img_x=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
img_y=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
# cv2.imshow("Anh goc",img)
# cv2.imshow("Sobel X",img_x)
# cv2.imshow("Sobel Y",img_y)
laplacian=cv2.Laplacian(img,cv2.CV_32F,ksize=9,scale=1,delta=0)
cv2.normalize(laplacian,laplacian,alpha=0,beta=1,norm_type=cv2.NORM_MINMAX)
cv2.imshow("image",img)
cv2.imshow("laplacian",laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()
