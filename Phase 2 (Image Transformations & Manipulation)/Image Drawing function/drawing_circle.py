import cv2

image=cv2.imread('D:\Open CV\Phase 2 (Image Transformations & Manipulation)\Image Drawing function\images.jpeg')

if image is None:
    print("Error: Could not read the image.")

else:
    print("Image loaded")

    center=(100,100)
    radius=50
    color=(255,0,0)
    thickness=-1      #for filled circle, use -1

    cv2.circle(image,center,radius,color,thickness)

    cv2.imshow("Circle Drawing",image)
    cv2.waitKey(0)
    cv2.distroyAllWindows
