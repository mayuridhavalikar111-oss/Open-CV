import cv2

image=cv2.imread(input("Enter the location of the image:"))

n=int(input("Enter the number to select the function to perform on the image:\n1. Draw a line\n2. Draw a rectangle\n3. Draw a circle\n4. Add text\n"))

if image is None:
    print("Error: Could not read the image.")

else:
    print("Image loaded")

    #DRAW LINE
    if n==1:
        x1=int(input("Enter the x coordinate of the first point:"))
        y1=int(input("Enter the y coordinate of the first point:"))
        x2=int(input("Enter the x coordinate of the second point:"))
        y2=int(input("Enter the y coordinate of the second point:"))

        pt1=(x1,y1)
        pt2=(x2,y2)
        color=(255,0,0)
        thickness=2

        line=cv2.line(image, pt1,pt2,color,thickness)
        cv2.imshow("Image", image)
        
        save=int(input("Do you want to save this image? (1.Yes or 2.NO)"))
        if save==1:
            cv2.imwrite("Output_image",line)
            print("Output image saved")
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    #DRAW RECTANGLE
    elif n==2:
            x1=int(input("Enter the x coordinate of the first point:"))
            y1=int(input("Enter the y coordinate of the first point:"))
            x2=int(input("Enter the x coordinate of the second point:"))
            y2=int(input("Enter the y coordinate of the second point:"))

            pt1=(x1,y1)
            pt2=(x2,y2)
            color=(255,0,0)
            thickness=2
    
            rectangle=cv2.rectangle(image, pt1,pt2,color,thickness)
            cv2.imshow("Image", image)
            
            save=int(input("Do you want to save this image? (1.Yes or 2.NO)"))
            if save==1:
                cv2.imwrite("Output_image",rectangle)
                print("Output image saved")
            
            cv2.waitKey(0)
            cv2.destroyAllWindows()

#DRAW CIRCLE
    elif n==3:
        x=int(input("Enter the x coordinate of the center:"))
        y=int(input("Enter the y coordinate of the center:"))
        radius=int(input("Enter the radius of the circle:"))

        color=(255,0,0)
        thickness=2

        circle=cv2.circle(image, (x,y), radius, color, thickness)
        cv2.imshow("Image", image)

        save=int(input("Do you want to save this image? (1.Yes or 2.NO)"))
        if save==1:
            cv2.imwrite("Output_image",circle)
            print("Output image saved")

        cv2.waitKey(0)
        cv2.destroyAllWindows()

#ADD TEXT
    elif n==4:
        text=input("Enter the text to be added:")
        x=int(input("Enter the x coordinate of the starting point:"))
        y=int(input("Enter the y coordinate of the starting point:"))

        org=(x,y)
        font=cv2.FONT_HERSHEY_COMPLEX
        fontScale=1.0
        color=(255,0,0)
        thickness=2

        text_added=cv2.putText(image,text,org,font,fontScale,color,thickness)
        cv2.imshow("Image", image)

        save=int(input("Do you want to save this image? (1.Yes or 2.NO)"))
        if save==1:
            cv2.imwrite("Output_image",text_added)
            print("Output image saved")

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:
        print("Invalid input. Please select a number between 1 and 4.")
        