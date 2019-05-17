import pyautogui
import time

for i in range(1,10,1):
    pyautogui.moveTo(1000, 600)
    time.sleep(.3)
    pyautogui.moveTo(1200, 600)
    time.sleep(.3)
    print(i)

print("fim")	
