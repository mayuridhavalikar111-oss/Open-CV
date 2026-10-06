import cv2
img=cv2.imread('D:/Open CV/Phase 6 (Contors & Shape Detection)/random_image.jpeg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)      #Displaying contour
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)     #Find conntour
cv2.drawContours(img,contours,-1,(0,255,0),3)

cv2.imshow('Contours',img)
cv2.waitKey(0)
cv2.destroyAllWindows
