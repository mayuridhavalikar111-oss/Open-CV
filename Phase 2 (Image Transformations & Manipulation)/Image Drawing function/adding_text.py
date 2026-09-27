import cv2

image=cv2.imread('D:\Open CV\Phase 2 (Image Transformations & Manipulation)\Image Drawing function\images.jpeg')

if image is None:
    print("Error: Could not read the image.")

else:
    print("Image loaded")

    text="Hello"
    org=(50,50)
    font=cv2.FONT_HERSHEY_COMPLEX
    fontScale=1.0
    color=(255,0,0)
    thickness=1

    cv2.putText(image,text,org,font,fontScale,color,thickness)

    cv2.imshow("TEXT PRINTRD",image)
    cv2.waitKey(0)
    cv2.distroyAllWindows
