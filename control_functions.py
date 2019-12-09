import pyautogui #screenshot
import time
from winsound import Beep #for beep sounds
import uuid #random string generator
import tkinter
from tkinter import messagebox as tkMessageBox


#___________random string generation______________
def my_random_string(string_length=10):
    #"""Returns a random string of length string_length."""
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.upper() # Make all characters uppercase.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length] # Return the random string.


#__________CLASS OF CONTROL FUNCTIONS_______
        

def quitfunction():
    exit()

def screenshoot():
    imagename=my_random_string(6)
    im1=pyautogui.screenshot('F:/IMAGE '+ str(imagename)+'.png')
    tkMessageBox.showinfo( "Hello user", "This PC>>F: is path location of your screenshot")

def beep_sound():
    Beep(1000,300)
