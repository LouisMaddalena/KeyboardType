
import pyautogui, sys, time

def main():

    if len(sys.argv) == 0:
        print("No argument found, please provide arguments within quotes")
    elif len(sys.argv) > 2:
        print("Too many arguments presnt plaease provide text to paste within quotes.")

    time.sleep(1) #sleep giving user ability to run script and move curser to correct location. Comment out if using in in alfred/streamdeck

    for i in range(len(sys.argv[1])):
        if sys.argv[1][i] == "\n":  #protects against sending messages in chat platform when pasting. Slows down overall performance. 
            pyautogui.keyDown("shift")
            pyautogui.press("enter")
            pyautogui.keyUp("shift")
        else:
            pyautogui.typewrite(str(sys.argv[1][i])) #only this line is required if you do not want to protect against sending pasted content a chat platform



main()
