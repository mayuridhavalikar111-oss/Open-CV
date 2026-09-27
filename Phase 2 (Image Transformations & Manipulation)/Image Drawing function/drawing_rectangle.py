import cv2

image=cv2.imread('D:\Open CV\Phase 2 (Image Transformations & Manipulation)\Image Drawing function\images.jpeg')

if image is None:
    print("Error: Could not read the image.")

else:
    print("Image loaded")

    pt1=(50,50)
    pt2=(150,100)
    color=(255,0,0)
    thickness=3

    cv2.rectangle(image, pt1,pt2,color,thickness)

    cv2.imshow("Rectangle Drawing",image)
    cv2.waitKey(0)
    cv2.distroyAllWindows
