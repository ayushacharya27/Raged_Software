import cv2
bbox_x1 = input("Enter the Starting X Point of Bbox: ")
bbox_x2 = input("Enter the Ending X Point of Bbox: ")

distance = input("Enter the Distance From Camera: ")

Width = input("Enter the Actual Width: ")
 
image = cv2.imread("camera_calib.py")
width_pixels = bbox_x2 - bbox_x1

print((width_pixels*distance)/Width)



    
    



