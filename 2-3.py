import cv2
import numpy as np
img=cv2.imread("logo.png")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

output=np.zeros(img_gray.shape,img_gray.dtype)
h,w=img_gray.shape
alpha=1.3
beta=50

for y in range(h):
    for x in range(w):
        output[y,x]=np.clip(alpha*img_gray[y,x]+beta,0,255)
        