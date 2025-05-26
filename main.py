import keyboard
import pyautogui
from time import sleep
try:
    print("Media control active. Press ctrl+alt+esc to exit")
    keyboard.add_hotkey('ctrl+alt+p', lambda: pyautogui.press('playpause'), sleep(0.5))
    keyboard.add_hotkey('ctrl+alt+right', lambda: pyautogui.press('nexttrack'), sleep(0.5))
    keyboard.add_hotkey('ctrl+alt+left', lambda: pyautogui.press('prevtrack'), sleep(0.5))
    keyboard.add_hotkey('ctrl+alt+up', lambda: pyautogui.press('volumeup'), sleep(0.5))
    keyboard.add_hotkey('ctrl+alt+down', lambda: pyautogui.press('volumedown'), sleep(0.5))
    keyboard.add_hotkey('ctrl+alt+m', lambda: pyautogui.press('volumemute'), sleep(0.5))

    keyboard.wait('ctrl+alt+esc')
except KeyboardInterrupt:
    print("Program was forcibly stopped by the user")
except Exception as e:
    print(f"[!] Error {e}")