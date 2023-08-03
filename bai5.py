import cv2
img = cv2.imread("anh-dep-23.png")
[w,h,c]=img.shape
print("h:",h,"w:",w,"c:",c)
# cv2.imshow("anh goc",img)
px=img[20,30]# lấy giá trị của điểm ảnh
print("px:",px)
sh=img.shape # lấy kích thước của ảnh

# cv2.imshow("anh xam",img_gray)

img = cv2.resize(img,(320,240))
img_gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
for i in range(135,185):
    for j in range(95,145):
        img[j,i]=(0,255,0)


# for i in range(135,185):
#     for j in range(95,145):
#         img_gray[j,i]=(255)
# for i in range(320):
#     for j in range(240):
#         if img_gray[j,i]==(255):
#             continue
#         else:
#             img_gray[j,i]=(0)

print('pixel:',px)
cv2.imshow("anh thay doi",img) 
cv2.imshow("anh thay doi",img_gray)  

# t,maskI=cv2.threshold(img,125,255,cv2.THRESH_BINARY)
# cv2.imshow("binary",maskI)
# t,maskII=cv2.threshold(img,125,255,cv2.THRESH_BINARY_INV)
# cv2.imshow("binary1",maskII)

# imgAND =cv2.bitwise_and(img,img_gray,mask=None)
# cv2.imshow("AND",imgAND)
# imgANDmask=cv2.bitwise_and(img,img_gray,mask=maskI)
# cv2.imshow("AND mask",imgANDmask)
cv2.waitKey(0)
cv2.destroyAllWindows()
