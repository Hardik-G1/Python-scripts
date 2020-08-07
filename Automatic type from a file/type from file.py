import pynput
import time
from pynput.keyboard import Key,Controller
k=Controller()
time.sleep(12)# without it will type instantly
file=open("fcfs.txt")
for i in file:
    k.type(i.lstrip())
    time.sleep(0.5)
