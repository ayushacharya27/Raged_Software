# Camera HFoV = 70 Degrees

import cv2
import mediapipe as mp

def calculate_angle(x,width):
    center = width/2
    theta_per_degree = 70/width

    error = x - center
    angle = error * theta_per_degree

    return angle




# Calling Function to Draw Hands
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

video = cv2.VideoCapture(0)
hands = mp_hands.Hands()

while True:
    ret , frame = video.read()
    if not ret: 
        print("Camera not Yet Open")
        break

    # Making Frame as Black and White
    frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)

    results = hands.process(frame)

    height,width,_ = frame.shape

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame , hand_landmarks , mp_hands.HAND_CONNECTIONS)

            index_tip = hand_landmarks.landmark[8]
            cx, cy = int(index_tip.x * width), int(index_tip.y * height)
            angle = calculate_angle(cx,width)

            cv2.circle(frame, (cx, cy), 10, (0, 0, 255), -1)

            '''cv2.putText(frame, f"Index Tip: ({cx}, {cy})", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)'''
            
            # Put Angle in Text Format 
            cv2.putText(frame, f"Angle: ({angle}*)", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    
    cv2.imshow("Index Finger Tracking", frame)

    if cv2.waitKey(1)==ord('q'):
        break

video.release()
cv2.destroyAllWindows()






