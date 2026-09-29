import cv2
image=cv2.imread('D:/Open CV/Phase 4 (Image Filtering & Blurring)/random_image.jpeg')

blurred=cv2.GaussianBlur(image,(7,7),0)

cv2.imshow("Original image",image)
cv2.imshow("Blurred image",blurred)

cv2.waitKey(0)
cv2.destroyAllWindows
