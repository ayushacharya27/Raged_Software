import pandas as pd
import serial
import time
import keyboard
import os

# Creating an Empty List
data = []

# Initialising Arduino and its COM Port
arduino = serial.Serial("COM3", 9600, timeout=1)

# Enter minus value of angle if the object is present in "Left" and plus value of angle if the object present in "Right" 
angle = input("Enter the angle: ")
file_exists = os.path.isfile('angle_dataset.csv')
while True:
    
    if keyboard.is_pressed('a'):
        # Sending Value to Arduino
        arduino.write(b'a')
        current_time = time.time()
        while keyboard.is_pressed('a'):
            pass

        # Sending Value to Arduino to Stop What it's Doing
        arduino.write(b'm')

        final_time = time.time()

        time_pressed =  -(final_time - current_time) # minus sign for obstacle present in left
        data.append({"Angle": angle , "Time":time_pressed*1000})
        df = pd.DataFrame(data)
        df.to_csv('angle_dataset.csv',mode='a', index=False, header=not file_exists)
        print(time_pressed)
    
    if keyboard.is_pressed('d'):

        # Sending Value to Arduino
        arduino.write(b'd')

        current_time = time.time()
        while keyboard.is_pressed('d'):
            pass

        # Sending Value to Arduino to Stop What it's Doing
        arduino.write(b'm')

        final_time = time.time()

        time_pressed =  final_time - current_time # plus sign for obstacle present in right
        data.append({"Angle":angle , "Time":time_pressed*1000})
        df = pd.DataFrame(data)
        df.to_csv('angle_dataset.csv',mode='a', index=False, header=not file_exists)
        print(time_pressed)


    if keyboard.is_pressed('esc'):
        print("Exiting the loop")
        break


print("Data Saved to Csv File") 