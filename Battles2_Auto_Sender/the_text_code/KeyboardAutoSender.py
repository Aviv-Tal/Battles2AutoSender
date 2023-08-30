from keyboard import read_key, press, release
from mouse import is_pressed as pressed, wait
from time import sleep
from pyautogui import hotkey
import Utility as util
import pyautogui

def keyboardAutoSend(legal_keys: list):
    last_key = "l"
    while True:
        key = read_key()
        if key == "z":
            pyautogui.press(last_key)
            continue
        if key not in legal_keys:
            continue
        pyautogui.press(last_key)
        sleep(0.1)
        pyautogui.hotkey(key, "alt") #TODO - make this work
        last_key = key
        
        
if __name__ == "__main__":
    try:
        f = open(util.path_to_variables, "r")
        legal_keys = util.getSendHotKeys(f.readlines())
        keyboardAutoSend(legal_keys)
    except Exception as e:
        input(f"Exception {e}")