import cv2
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while(True):
    ret,frame = cap.read()
    tshape = frame.shape
    t1=frame.shape[0]
    t2=frame.shape[2]
    print("shape:",tshape)
    print("shape(0): ",t1,"t2",t2)
    cv2.imshow('Video from camera PC',frame)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
