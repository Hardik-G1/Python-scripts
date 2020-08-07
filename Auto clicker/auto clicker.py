from pynput.mouse import Button, Controller
mouse = Controller()
print ("Current position: " + str(mouse.position))
#set the positon of mouse to x and y coordinates
mouse.position = (100, 200)
n=int(input("how many clicks"))
option=int(input("for right click -> 0\nfor left click->1"))
if option==1:
    mouse.click(Button.left, n)
else:
    mouse.click(Button.right,n)
##other commands##
##mouse.press(Button.left)
##mouse.release(Button.left)
### Scroll up two steps
##mouse.scroll(0, 2)
### Scroll right five steps
##mouse.scroll(5, 0)
