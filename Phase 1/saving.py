import cv2
image=cv2.imread("D:\Open CV\python.jpeg")

if image is not None:
    success=cv2.imwrite("output_python.png",image)
    if success:
        print("Image saved successfully.")
    else:
        print("Error: Could not save image.")
else:
    print("Error: Could not load image.")

#This will create a new file named "output_python.png" in the current working directory with the same content as the original image.
