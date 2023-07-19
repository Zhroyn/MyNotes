from pynput import mouse
from pynput import keyboard
import time
import threading
import sys


class mouseController(threading.Thread):
    def __init__(self, click_times, internal):
        threading.Thread.__init__(self)
        self.click_times = click_times
        self.internal = internal

    def run(self):
        control = mouse.Controller()
        i = 0
        while(i < self.click_times):
            control.click(mouse.Button.left, 1)
            time.sleep(self.internal)
            i += 1


def on_press(key):
    click_thread = mouseController(2100, 0.02)
    if key == keyboard.Key.space:
        click_thread.start()
    elif key == keyboard.Key.esc:
        sys.exit()

def listen_keyboard():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    listen_keyboard()