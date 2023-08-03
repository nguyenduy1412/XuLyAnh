import cv2
import time

# Khởi tạo đối tượng VideoCapture
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
while True:
    # Đọc khung hình
    ret, frame = cap.read()

    # Hiển thị khung hình
    cv2.imshow("Video", frame)

    # Chờ 5 giây
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('s'):
        time.sleep(5)

        # Đọc khung hình
        ret, frame = cap.read()

        # Lưu ảnh
        cv2.imwrite("capture.jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
        
cap.release()
cv2.destroyAllWindows()