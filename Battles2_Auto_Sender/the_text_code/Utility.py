from pyautogui import hotkey
from typing import Optional
from ctypes import wintypes, windll, create_unicode_buffer

path_to_variables = "..\\important files\\Variables.txt"
path_to_borders = "..\\important files\\Borders.txt"

# get the keys to send bloons from the variables file
def getSendHotKeys(file_content: list) -> list:
    keys = file_content[1].split("=")[1].strip()
    return keys[1:-1].split(",")

def exitGame():
    hotkey("alt", "f4")
    
def getActiveWindow() -> Optional[str]:
    hWnd = windll.user32.GetForegroundWindow()
    length = windll.user32.GetWindowTextLengthW(hWnd)
    buf = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(hWnd, buf, length + 1)
    
    # 1-liner alternative: return buf.value if buf.value else None
    if buf.value:
        return buf.value
    else:
        return None