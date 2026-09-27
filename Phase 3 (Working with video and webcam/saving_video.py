import cv2
camara=cv2.VideoCapture(0)

frame_width=int(camara.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height=int(camara.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec=cv2.VideoCapture
recorder=cv2.VideoWriter("Output_video.avi",cv2.VideoWriter_fourcc(*'XVID'),20,(frame_width,frame_height))
while True:
    success,image=camara.read()
    if not success:
        break
    recorder.write(image)
    cv2.imshow("Video",image)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
camara.release()
recorder.release()
cv2.destroyAllWindows()