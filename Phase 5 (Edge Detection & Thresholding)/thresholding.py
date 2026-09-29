import cv2

image=cv2.imread('D:\\Open CV\\Phase 5 (Edge Detection & Thresholding)\\random_image.jpeg',cv2.IMREAD_GRAYSCALE)
ret, thresh_img=cv2.threshold(image,120,255,cv2.THRESH_BINARY)      #(image,threshold_value,max_value,thresholding_type)

cv2.imshow("Original image",image)
cv2.imshow("Thresholded Image",thresh_img) 

cv2.waitKey(0)
cv2.destroyAllWindows
