import cv2
image=cv2.imread('D:\Open CV\Phase 2 (Image Transformations & Manipulation)\images.jpeg')  # Load the image from file
if image is None:
    print("Error: Could not read the image.")
else:
    print("Image loaded")

    flipped_horizontal=cv2.flip(image,1)
    flipped_vertical=cv2.flip(image,0)
    flipped_both=cv2.flip(image,-1)
   
    cv2.imshow("Original image:", image)
    cv2.imshow("Flipped Horizontal",flipped_horizontal)
    cv2.imshow("Flipped Vertical",flipped_vertical)
    cv2.imshow("Flipped Both",flipped_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    