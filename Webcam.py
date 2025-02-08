import cv2

def ShowVideo(event):
    # Change the Number According to Your Webcam Port Number
    video = cv2.VideoCapture(0) #  0 here because we are using internal webcam here

    while(True):
        ret,frame = video.read()
        if not ret:
            print("Check Connection Dawg")
            break

        # Name the Frame as Webcam
        cv2.imshow('Webcam', frame)

        # Press q to Exit the Simulation
        if cv2.waitKey(1) == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()