import cv2
from Webcam import ShowVideo

clicked_point = None 
def mouse_click(event , x , y , flags , param ):
    if event == cv2.EVENT_LBUTTONDOWN:
        global clicked_point
        print(x,"",y)
        clicked_point = (x,y)


# Change the Number According to Your Webcam Port Number
video = cv2.VideoCapture(0) #  0 here because we are using internal webcam here

while(True):
    ret,frame = video.read()
    if not ret:
        print("Check Connection Dawg")
        break
    if clicked_point :
        cv2.circle(frame , clicked_point , 10, (0, 255, 0), -1)
    # Name the Frame as Webcam
    cv2.imshow('Webcam', frame)
    cv2.setMouseCallback('Webcam', mouse_click) 

    # Press q to Exit the Simulation
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

