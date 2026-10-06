import cv2
img=cv2.imread('D:/Open CV/Phase 6 (Contors & Shape Detection)/random_image.jpeg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)      #Displaying contour
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)     #Find conntour
cv2.drawContours(img,contours,-1,(0,255,0),3)

#Detecting shape
for contour in contours:
    approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    corners=len(approx)
    
    if len(approx)==3:
        cv2.putText(img,"Triangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
    elif len(approx)==4:
        cv2.putText(img,"Rectangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
    elif len(approx)==5:
        cv2.putText(img,"Pentagon",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
    elif len(approx)==6:
        cv2.putText(img,"Hexagon",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
    else:
        cv2.putText(img,"Circle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)


cv2.imshow('Contours',img)
cv2.waitKey(0)
cv2.destroyAllWindows
