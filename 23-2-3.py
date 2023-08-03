import cv2
import numpy as np
A=50
B=150
img=cv2.imread('yourname.jpg',0)
img=cv2.resize(img,(640,480))
h,w=img.shape
img_gls=np.array(img.copy())

img_gls1=np.where(((img_gls>A) & (img_gls<B)),255,0)
img_gls1=img_gls1.astype(np.uint8)
cv2.imshow('anh goc',img)
cv2.imshow('khong nen',img_gls1)

img_gls2=np.where(((img_gls1>A) & (img_gls <B)),255,100)
img_gls2=img_gls2.astype(np.uint8)
cv2.imshow('Nen',img_gls2)
cv2.waitKey(0)
cv2.destroyAllWindows()