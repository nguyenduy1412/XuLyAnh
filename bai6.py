import cv2
import numpy as np
img =cv2.imread('images.png',0)
img1 = cv2.imread('anh-dep-23.png',0)
img=cv2.resize(img,(640,480))
img1=cv2.resize(img1,(640,480))
img_sub=cv2.subtract(img1,img)
cv2.imshow('image',img_sub)
cv2.waitKey(0)
cv2.destroyAllWindows()