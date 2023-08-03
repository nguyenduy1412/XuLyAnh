import cv2
import numpy as np
img=cv2.imread('yourname.jpg')
img=cv2.resize(img,(640,480))
gamma=0.2
img_constr=np.power(img,gamma)
max_val=np.max(img_constr.ravel())
img_constr=img_constr/max_val *255
img_constr=img_constr.astype(np.uint8)
cv2.imshow('anh goc',img)
cv2.imshow('anh tuong phan',img_constr)
cv2.waitKey(0)
cv2.destroyAllWindows()