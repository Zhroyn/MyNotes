from pynput import keyboard



def on_press(key):
    """按下按键时执行。"""
    try:
        print('{0} pressed'.format(
            key.char))
    except AttributeError:
        print('{0} pressed'.format(
            key))
    # 通过属性判断按键类型。


def on_release(key):
    """松开按键时执行。"""
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released





def listen_keyboard():
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


def control_keyboard():
    control = keyboard.Controller()

    control.press(keyboard.KeyCode.from_vk(65))
    control.release('a')
    control.press(keyboard.Key.ctrl)
    control.release(keyboard.Key.ctrl)
    control.press('s')
    control.release('s')

    with keyboard.Controller.pressed(
        keyboard.Key.ctrl,
        keyboard.Key.shift,
        's'):
        pass    #进入语句时顺序按下提供的按键，退出时逆序释放按键

    control.type([keyboard.Key.esc])
    control.type('你好!')

listen_keyboard() 