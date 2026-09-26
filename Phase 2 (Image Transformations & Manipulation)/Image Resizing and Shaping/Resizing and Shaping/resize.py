import cv2
image=cv2.imread('D:\Open CV\Phase 2 (Image Transformations & Manipulation)\python.jpeg')  # Load the image from file
if image is None:
    print("Error: Could not read the image.")
else:
    print("Image loaded")
    resize=cv2.resize(image,(300,300))   #Resize the image to 300x300 pixels
    cv2.imshow("Original image:", image)
    cv2.imshow("Resized image:", resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    