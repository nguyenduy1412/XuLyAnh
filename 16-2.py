import cv2
import numpy as np

# Đọc ảnh RGB
img_rgb0 = cv2.imread('yourname.jpg')
img_rgb=cv2.resize(img_rgb0,(640,480))

# Chuyển đổi sang HSV
img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2HSV)

# Tính giá trị V_max và V_min
V_max = np.max(img_hsv[:,:,2])
V_min = np.min(img_hsv[:,:,2])

# Tính giá trị pixel mới cho kênh V
V_new = ((img_hsv[:,:,2] - V_min) * (255 / (V_max - V_min))).astype(np.uint8)

# Gán lại kênh V của ảnh HSV
img_hsv[:,:,2] = V_new

# Chuyển đổi sang LHSV
img_lhsv = np.zeros_like(img_hsv)
img_lhsv[:,:,0] = img_hsv[:,:,0]
img_lhsv[:,:,1] = img_hsv[:,:,1]
img_lhsv[:,:,2] = (img_hsv[:,:,0] + img_hsv[:,:,1] + img_hsv[:,:,2]) / 3

# Chuyển đổi sang HSV
img_hsv_new = np.zeros_like(img_hsv)
img_hsv_new[:,:,0] = img_lhsv[:,:,0]
img_hsv_new[:,:,1] = img_lhsv[:,:,1]
img_hsv_new[:,:,2] = img_lhsv[:,:,2]
img_hsv_new = img_hsv_new.astype(np.uint8)

# Chuyển đổi sang RGB
img_out = cv2.cvtColor(img_hsv_new, cv2.COLOR_HSV2BGR)

# Hiển thị ảnh I mới
cv2.imshow('image', img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
