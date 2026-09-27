import cv2
image=cv2.imread('D:\Open CV\Phase 2 (Image Transformations & Manipulation)\images.jpeg')  # Load the image from file
if image is None:
    print("Error: Could not read the image.")
else:
    print("Image loaded")

    (h,w)=image.shape[:2]
    center=(w//2,h//2)
    M=cv2.getRotationMatrix2D(center,90,1.0)
    rotated_image=cv2.warpAffine(image,M,(w,h))
   
    cv2.imshow("Original image:", image)
    cv2.imshow("Rotated 90 degree image",rotated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    