import psutil
from pynput.keyboard import Key, Listener
from time import sleep
def on_press(key):
    return True
def on_release(key):
    if key == Key.alt_r:
        return False
listener=Listener(on_press=on_press,on_release=on_release)
listener.start()
while (listener.is_alive()):
    for proc in psutil.process_iter():
        if any(procstr in proc.name() for procstr in\
            ['Taskmgr']):
            print('Killing Taskmanager')
            proc.kill()
                


