import pandas as pd
import serial
import time
import keyboard
import os
data = []
arduino = serial.Serial("COM3", 9600, timeout=1)
distance = input("Enter the Current_Distance: ")
file_exists = os.path.isfile('distance_dataset.csv')
while True:
    
    if keyboard.is_pressed('w'):
        arduino.write(b'w')
        current_time = time.time()
        while keyboard.is_pressed('w'):
            pass
        arduino.write(b'm')
        final_time = time.time()

        time_pressed =  final_time - current_time
        data.append({"Distance: ": distance , "Time: ":time_pressed*1000})
        df = pd.DataFrame(data)
        df.to_csv('distance_dataset.csv',mode='a', index=False, header=not file_exists)
        print(time_pressed)
    if keyboard.is_pressed('esc'):
        print("Exiting the loop")
        break


print("Data Saved to Csv File")