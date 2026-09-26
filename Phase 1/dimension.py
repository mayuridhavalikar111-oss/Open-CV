import cv2
image=cv2.imread("D:\Open CV\python.jpeg")

if image is not None:
    h,w,c=image.shape
    print("Image loaded:\n Height:",h,"\nWidth:",w,"\nChannels:",c)
else:
    print("Error: Could not load image.")

'''Output:
Image loaded:
 Height: 148 
Width: 244 
Channels: 3'''