import cv2
import numpy as np
img=cv2.imread('lena.png')
cv2.imshow('Anh goc',img)
#lọc ảnh với cửa sổ 3x3
img_mean0=cv2.blur(img,(3,3))
cv2.imshow('Anh loc trung binh cua so 3x3',img_mean0)
s=[(3,3),(5,5),(7,7),(9,9)]
# for i,k in enumerate(s):
#     img_mean=cv2.blur(img,k)
#     cv2.imwrite(f'anh_trungbinh_{i}.png',img_mean)
#     cv2.imshow(f'Anh trung binh {i}',img_mean)
# img_mean1=cv2.blur(img,(9,9))
# gamma=1.8
# img_constr=np.power(img_mean1,gamma)
# max_val=np.max(img_constr.ravel)
#thuc hien voi nhieu cua so loc kich thuoc khác nhau
img_gaus=cv2.GaussianBlur(img,(5,5),0)
cv2.imwrite('anhgaussian.png',img_gaus)
cv2.imshow('Anh goc',img_gaus)
cv2.imshow('Gaussian Blurring',img_gaus)
img_median=cv2.medianBlur(img,7)
cv2.imwrite('anhtrungvi.png',img_median)
cv2.imshow('anh trung vi',img_median)
img2=cv2.resize(img(320,240))
img_bilateralFiler=cv2.bilateralFilter(img,9,75,75)
img_bilateralFiler=cv2.bilateralFilter(img2,7,7,75,75)
cv2.waitKey(0)
cv2.destroyAllWindows()
