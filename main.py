import time

import serial
import keyboard
import pyautogui

# Serial takes two parameters: serial device and baudrate
ser = serial.Serial('COM7', 9600)
while True:
    d = ser.readline()

    if d:
        s = d.decode('utf-8').strip()
        match s:
            case "FFC23D":
                print("Play/Pause COMMAND")
                pyautogui.press('playpause')
                ser.write(b'Play/Pause SUCCESS')
            case "FF02FD":
                print("Skip COMMAND")
                pyautogui.press('nexttrack')
                ser.write(b'Skip SUCCESS')
            case "FF22DD":
                print("Previous COMMAND")
                pyautogui.press('prevtrack')
                ser.write(b'Previous SUCCESS')
            case "FFA857":
                print("Volume UP COMMAND")
                pyautogui.press('volumeup', presses=5)
                ser.write(b'Volume UP SUCCESS')
            case "FFE01F":
                print("Volume DOWN COMMAND")
                pyautogui.press('volumedown', presses=5)
                ser.write(b'Volume DOWN SUCCESS')
            case "FF906F":
                print("EQ COMMAND")
                pyautogui.press('volumemute')
                ser.write(b'EQ SUCCESS')
            case "FF629D":
                print("CH COMMAND")
                pyautogui.hotkey('alt', 'tab')
                ser.write(b'CH SUCCESS')
            case "FFA25D":
                print("CH- COMMAND")
                pyautogui.hotkey('win', 'd')
                ser.write(b'CH- SUCCESS')
            case "FFE21D":
                print("CH+ COMMAND")
                pyautogui.hotkey('alt', 'shift', 'tab')
                ser.write(b'CH+ SUCCESS')
        print(s)
    continue
