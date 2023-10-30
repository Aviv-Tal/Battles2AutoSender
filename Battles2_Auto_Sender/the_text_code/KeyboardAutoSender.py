from keyboard import read_key, press, release
from mouse import is_pressed as pressed, wait
from time import sleep
from pyautogui import hotkey
import Utility as util
from sys import stdout
from os import system


def keyboardAutoSend(legal_keys: list):
    text = f"**********\nPRESSING T\n**********"
    key = read_key()

    if key not in legal_keys:
        return
    
    system("cls")
        
        
    cap_key = key.capitalize()
    text = f"**********\nPRESSING {cap_key}\n**********"
    stdout.write(text)
    stdout.flush()
    
    while True:
        if util.isBattlesOpen():
            press(key)
            sleep(0.05)
            if pressed(button="right"):
                break
        else:
            if not util.isBattlesRunning():
                exit()
            release(key)
            sleep(0.1)
    release(key)
    
    system("cls")
        
    stdout.flush()
    stdout.write("**********\nWAITING FOR NEW INPUT\n**********")
    stdout.flush()
        
if __name__ == "__main__":
    f = open(util.path_to_variables, "r")
    legal_keys = util.getSendHotKeys(f.readlines())
    keyboardAutoSend(legal_keys)