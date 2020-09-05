import pyautogui # Importing pyautogui
import time # Importing time for sleep and pause

time.sleep(5) #startup time [sleep]

letter = open("script.txt" , 'r') #opening script file
for word in letter: #for loop
    pyautogui.typewrite(word) #typing words
    pyautogui.press("enter") #pressing keys
    #end of code
