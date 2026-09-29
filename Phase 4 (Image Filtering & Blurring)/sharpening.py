import cv2
import numpy as np

image=cv2.imread('D:/Open CV/Phase 4 (Image Filtering & Blurring)/random_image.jpeg')

sharpen_kernel=np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])

sharpened=cv2.filter2D(image,-1,sharpen_kernel)

cv2.imshow("Original image",image)
cv2.imshow("Sharpened image",sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows
