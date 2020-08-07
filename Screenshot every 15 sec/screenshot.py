import pyautogui
from pathlib import Path
from time import sleep
i=0
while True:
    sleep(15)
    myScreenshot = pyautogui.screenshot()
    dir='directory/path/here'
    b=str(i)
    c='.png'
    x=Path(dir,b).with_suffix(c)
    myScreenshot.save(x)
    i+=1
