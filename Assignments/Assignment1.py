file_name=input("Enter the image file name (with extension): ")
import cv2

image=cv2.imread(file_name)    #load image

gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    #convert to grayscale
cv2.imshow("Image showing", gray)    #display Gray image

n=int(input("Enter a number of your choice:\n 1. Save Image\n 2. Display Image\n"))    #take input from user

if n==1:
    out_file_name=input("Enter name of the output file (with extension): ")

    cv2.imwrite(out_file_name, image)    #save image
    print("Image saved successfully as:", out_file_name)

else:
    cv2.imshow("Image showing", image)    #display image
    cv2.waitKey(0)
    cv2.destroyAllWindows()
