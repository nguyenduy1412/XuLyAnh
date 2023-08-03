import cv2
import numpy as np
def changePixelVal(pix,r1,s1,r2,s2):
    if(0<=pix and pix <=r1):
        return (s1/r1)*pix
    elif (r1 <pix and pix <=r2):
        return((s2-s1)/(r2-r1))*(pix -r1)+s1
    else:
        return ((255 -s2)/(255 -r2))*(pix-r2)+s2
img=cv2.imread('yourname.jpg')
img=cv2.resize(img,(640,480))


r1,s1,r2,s2=70,0,140,255
vec=np.vectorize(changePixelVal)
img1=vec(img,r1,s1,r2,s2)
cv2.imwrite("anh.png",img1)
cv2.imshow('anh goc',img)
cv2.imshow('anh bien doi tung khuc',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()