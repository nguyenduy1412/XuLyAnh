import cv2
import numpy as np

img=cv2.imread('Lenna.png',1)
# cv2.imshow('Anh',img)
img_mean0=cv2.blur(img,(9,9))
cv2.imshow('Anh loc trung binh cua so 9x9',img_mean0)
#chuyển sang không gian màu
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(img_hsv)
#làm trơn với kích thước cửa sổ 3x3
s_median = cv2.medianBlur(s, 3)
#ghép các kênh màu và chuyển sang rgb
img_hsv_median = cv2.merge([h, s_median, v])
img_median = cv2.cvtColor(img_hsv_median, cv2.COLOR_HSV2BGR)
cv2.imshow('Median filtered image', img_median)
v_median = cv2.medianBlur(v, 7)
img_hsv_median = cv2.merge([h, s, v_median])
img_median = cv2.cvtColor(img_hsv_median, cv2.COLOR_HSV2BGR)
cv2.imshow('Median filtered image', img_median)

cv2.waitKey(0)
cv2.destroyAllWindows()