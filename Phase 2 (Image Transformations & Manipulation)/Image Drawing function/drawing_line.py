import cv2

image=cv2.imread('D:\Open CV\Phase 2 (Image Transformations & Manipulation)\Image Drawing function\images.jpeg')

if image is None:
    print("Error: Could not read the image.")

else:
    print("Image loaded")

    pt1=(50,100)
    pt2=(100,100)
    color=(255,0,0)
    thickness=4

    cv2.line(image, pt1,pt2,color,thickness)

    cv2.imshow("Line Drawing",image)
    cv2.waitKey(0)
    cv2.distroyAllWindows
