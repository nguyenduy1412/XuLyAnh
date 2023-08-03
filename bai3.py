import cv2
fps = 20
vid_capture = cv2.VideoCapture(0)
# su dung phuong thuc get() de lay chieu rong va chieu cao cua khung hinh video
frame_width = int(vid_capture.get(3))
frame_height = int(vid_capture.get(4))
frame_size = (frame_width,frame_height)
#khoi tao doi tuong ghi video
output= cv2.VideoWriter('output_video_from_file.avi',cv2.VideoWriter_fourcc('M','J','P','G'),20,frame_size)
while(vid_capture.isOpened()):
    ret,frame=vid_capture.read()
    if ret==True:
        #Ghi frame vua doc duoc tu camera
        output.write(frame)
    else:
        print("Stream disconnected")
        break