from time import sleep
import pyautogui


msg = input("enter your Msg >>> ")
num_msg = int (input("chose your number of msg >>> "))
time_msg = float(input("chose your time of Msg >>> "))



for num in range (num_msg + 1):
    pyautogui.typewrite(msg)
    sleep(time_msg)
    pyautogui.press("enter")
    sleep(time_msg)
