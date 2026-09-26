import cv2
image=cv2.imread('D:\Open CV\Phase 2 (Image Transformations & Manipulation)\python.jpeg')  # Load the image from file
if image is None:
    print("Error: Could not read the image.")
else:
    print("Image loaded")
    cropped=image[100:200,100:200]   #Crop the image using slicing
    cv2.imshow("Original image:", image)
    cv2.imshow("Cropped image:", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    