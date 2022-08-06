import imagehash
import time
import pyautogui
import keyboard

while True:
    key = 'l'
    if keyboard.is_pressed('f'):
        im = pyautogui.screenshot(region=(955, 535, 10, 10)) # (x, y, width, height) change in case it doesn't match
        time.sleep(0.3)
        im2 = pyautogui.screenshot(region=(955, 535, 10, 10)) # same as above
        reticle = imagehash.average_hash(im)
        offset = imagehash.average_hash(im2)
        if reticle != offset:
            pyautogui.press('l')
