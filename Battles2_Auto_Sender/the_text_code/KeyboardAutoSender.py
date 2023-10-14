from keyboard import read_key, press, release
from mouse import is_pressed as pressed, wait
from time import sleep
from pyautogui import hotkey
import Utility as util

def keyboardAutoSend(legal_keys: list):
    while True:
        key = read_key()
        if key not in legal_keys:
            continue
        while True:
            if util.isBattlesOpen():
                press(key)
                sleep(0.05)
                if pressed(button="right"):
                    break
            else:
                release(key)
                sleep(0.05)
        release(key)
        
if __name__ == "__main__":
    f = open(util.path_to_variables, "r")
    legal_keys = util.getSendHotKeys(f.readlines())
    keyboardAutoSend(legal_keys)