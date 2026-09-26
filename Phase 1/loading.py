import cv2

image=cv2.imread("D:\Open CV\python.jpeg")

if image is None:
    print("Error: Could not load image.")
else:
    print("Image loaded successfully.")
