import cv2

img = cv2.imread("anh-dep-23.png")
tshape = img.shape
img1 = cv2.resize(img,(640,480))
t1=img.shape[0]
t2=img.shape[2]
img2=cv2.cvtColor(img1,cv2.COLOR_RGB2GRAY)
# print("shape:",tshape)
# print("shape(0): ",t1,"t2",t2)
# cv2.imshow("anh goc",img)
cv2.imshow("new",img1)
cv2.imshow("anh xam",img2)
cv2.waitKey(0)
cv2.destroyWindow()
# import cv2
# img = cv2.imread("anh-dep-23.png")
# [w,h,c]=img.shape
# print("h:",h,"w:",w,"c:",c)
# cv2.imshow("anh goc",img)
# px=img[20,30]
# print("px:",px)
