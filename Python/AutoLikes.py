import time
from pynput import mouse

def control_mouse(times):
    control = mouse.Controller()
    i = 0
    while(i < times):
        control.click(mouse.Button.left,1)
        time.sleep(0.02)
        i += 1

control_mouse(2100)