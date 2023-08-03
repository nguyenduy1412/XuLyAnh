import cv2
import numpy as np
img=cv2.imread("yourname.jpg")
[w,h,c]=img.shape
print("h:",h,"w:",w,"c:",c)
#cv2.imshow("anh goc",img)

img1=cv2.resize(img,(640,480))

# print("h1:",h1,"w1:",w1,"c1:",c1)

#cv2.imshow("anh",img1)
img_gray=cv2.cvtColor(img1,cv2.COLOR_RGB2GRAY)
cv2.imshow("anh xam",img_gray)
imgb,imgg,imgr=cv2.split(img1)
'''cv2.imshow('blue',imgb)
cv2.imshow('green',imgg)
cv2.imshow('red',imgr)'''
hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
h1,s1,v1= cv2.split(hsv)
'''cv2.imshow("H", h1)
cv2.imshow("S", s1)
cv2.imshow("V", v1)'''
# maxH=np.amax(h1)
# minH=np.amin(h1)
w1,h1,c1=img1.shape
img_gy=np.zeros((w1,h1),dtype="uint8")
img_gy=0.7*imgb+0.9*imgg+0.1*imgr
#cv2.imshow('Gray',img_gy)
img4=cv2.merge([imgb,imgg,imgr])
#cv2.imshow("newRGB",img4)
# print("Gia tri diem anh lon nhat cua kenh h la: ", maxH)
# print("Gia tri diem anh nho nhat cua kenh h la: ", minH)
# _,threshold = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# cv2.imshow("anh xam sang nguong otsu",threshold)
# _,threshold1 = cv2.threshold(img_gy, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# cv2.imshow("anh xam 1 sang nguong otsu",threshold1)
# giatri = 5
# y = 10
# x = 20
# for i in range(y-giatri//2, y+ giatri//2+1):
#     for j in range(x-giatri//2, x+giatri//2+1):
#         print("Pixel value at ({}, {}): {} ".format(i, j, img[i][j]))
img_neg=255-img_gray
cv2.imshow('anh am ban',img_neg)     
c=255/np.log(1+np.max(img_gray))
img_log=c*(np.log(img_gray+1))   
img_log=np.array(img_log,dtype=np.uint8)
cv2.imshow('anh bien doi log',img_log)

cv2.waitKey(0)
cv2.destroyAllWindows()