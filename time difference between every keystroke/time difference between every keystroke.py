from pynput.keyboard import Key, Listener
import time
def on_press(key):
    return True
def on_release(key):
    m=int(time.time()*1000)
    print(m)
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
