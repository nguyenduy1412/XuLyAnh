import cv2
img=cv2.imread("anh.png")
cv2.imshow("anh",img)
img1=cv2.resize(img,(320,240))
img5=cv2.resize(img,(320,240))
for i in range(90,170):
    for j in range(70,170):
        img1[j,i]=(255,255,255)
cv2.imshow("anh2",img1)
img2=cv2.resize(img,(320,240))
for i in range(150,240):
    for j in range(150,220):
        img2[j,i]=(255,255,255)
for i in range(120,170):
    for j in range(120,170):
        img5[i,j]=(255,255,255)
cv2.imshow('img5',img5)
cv2.imshow("anh1",img2)
#and
img_And=cv2.bitwise_and(img1,img2,mask=None)
cv2.imshow("anh and",img_And)
#or
img_or=cv2.bitwise_or(img1,img2,mask=None)
cv2.imshow("anh or",img_or)
img_gray=cv2.cvtColor(img5,cv2.COLOR_RGB2GRAY)
t,maskI=cv2.threshold(img_gray,120,255,cv2.THRESH_BINARY)
cv2.imshow("MASKI",maskI)
imgAND1=cv2.bitwise_and(img1,img2,mask=maskI)
cv2.imshow("AND mask",imgAND1)
img6=cv2.imread("chandung.jpg")
img6=cv2.resize(img6,(320,240))
img7=cv2.imread("nen.jpg")
img7=cv2.resize(img7,(320,240))
img_sub=cv2.subtract(img6,img7)
cv2.imshow("anh sub",img_sub)

cv2.waitKey(0)
cv2.destroyAllWindows()
