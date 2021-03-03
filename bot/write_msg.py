import pyautogui
from time import sleep
import os

class PyAutoGuiClass:
    def __init__(self):
        self.screenWidth, self.screenHeight = pyautogui.size()
        self.currentMouseX, self.currentMouseY = pyautogui.position()

    def pySpintaxSendDM1(self):
        #get msg1 from text file
        print("insdie pyspintax fun")
        sleep(5)
        pyautogui.moveTo(820,563)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        sleep(2)
        pyautogui.hotkey('ctrl', 'c')  
        sleep(2)

        pyautogui.moveTo(21,43) # click back
        pyautogui.click()
        sleep(10)
        pyautogui.moveTo(926, 642) # Move the mouse to XY coordinates.
        pyautogui.click()  
        pyautogui.hotkey('ctrl', 'v')   

        sleep(7)
        pyautogui.moveTo(1320, 955) # Move the mouse to XY coordinates.
        pyautogui.click() 

        sleep(12)

        pyautogui.moveTo(927, 835) # spintax result
        pyautogui.click() 
        sleep(5)

        pyautogui.hotkey('ctrl', 'c')  

        sleep(3)

        pyautogui.moveTo(21,43) # click back
        pyautogui.click()  
        sleep(10)

        pyautogui.moveTo(1277,1016) # click message box
        pyautogui.click()
        sleep(2) 

        pyautogui.hotkey('ctrl', 'v')
        sleep(5) 

    def pySpintaxComment(self):
        #get msg1 from text file
        print("insdie pyspintax comment fun")
        sleep(5)
        pyautogui.moveTo(820,563)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        sleep(2)
        pyautogui.hotkey('ctrl', 'c')  
        sleep(2)

        print("here 64")
        pyautogui.moveTo(21,43) # click back
        pyautogui.click()
        sleep(10)
        pyautogui.moveTo(926, 642) # Move the mouse to XY coordinates.
        pyautogui.click()  
        pyautogui.hotkey('ctrl', 'v')   

        sleep(5)
        pyautogui.moveTo(1320, 955) # Move the mouse to XY coordinates.
        pyautogui.click() 

        sleep(12)

        pyautogui.moveTo(927, 835) # spintax result
        pyautogui.click() 
        sleep(5)

        pyautogui.hotkey('ctrl', 'c')  

        sleep(3)

        pyautogui.moveTo(21,43) # click back
        pyautogui.click()  
        sleep(10)

        pyautogui.moveTo(926,388) # click message box
        pyautogui.click()
        sleep(2) 

        pyautogui.hotkey('ctrl', 'v')
        sleep(5)


# pyautogui.write('Hello world!', interval=0.25)
# pyautogui.write('\U0001f44d', interval=0.15)