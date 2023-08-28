import pyautogui
from time import sleep
from subprocess import call
import re
import Utility as util

def openBattles(file_content: list):
    path = file_content[0].split("=")[1].strip()
    call([path])
    
if __name__ == "__main__":
    openBattles()
