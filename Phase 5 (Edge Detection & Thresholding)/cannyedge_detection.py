import cv2

image=cv2.imread('D:\\Open CV\\Phase 5 (Edge Detection & Thresholding)\\random_image.jpeg',cv2.IMREAD_GRAYSCALE)
edges=cv2.Canny(image,50,150)      #(image,threshold1,threshold2)

cv2.imshow("Original image",image)
cv2.imshow("Canny Edges",edges) 

cv2.waitKey(0)
cv2.destroyAllWindows
