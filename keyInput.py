import pyautogui as pg
import time
# from pynput import keyboard

def scroll(num):
    scroll_count = 0
    while scroll_count < 67:
        pg.scroll(num)
        scroll_count += 1
    time.sleep(0.3)


def mouse_down():
    pg.moveTo(1200, 1000, duration=0.55)
    scroll(-50)

def move_mouse_and_click(top_left, bottom_right):
    print(top_left, bottom_right)
    pg.moveTo(top_left, bottom_right, duration=0.5)
    click()
    time.sleep(0.4)

def click():
    pg.click(clicks=1, interval=0, duration=0, button="left")
    time.sleep(0.4)


def open_card():
    pg.press(keys="F2", presses=1, interval=0.3)
    time.sleep(0.4)


def esc():
    pg.press(keys="esc", presses=1, interval=0.3)
    time.sleep(0.4)

def f():
    pg.press(keys="f", presses=1, interval=0.3)
    time.sleep(0.4)

def open_map():
    pg.press(keys="m", presses=1, interval=0.3)
    time.sleep(0.4)

def w(s):
    pg.keyDown('w')
    time.sleep(s)
    pg.keyUp('w')
    time.sleep(0.4)

def d(s):
    pg.keyDown('d')
    time.sleep(s)
    pg.keyUp('d')
    time.sleep(0.4)

def s(s):
    pg.keyDown('s')
    time.sleep(s)
    pg.keyUp('s')
    time.sleep(0.4)

def a(s):
    pg.keyDown('a')
    time.sleep(s)
    pg.keyUp('a')
    time.sleep(0.4)


def search(fn):
    s(1)
    if (fn()):
        f()
        return
    d(1)
    if (fn()):
        f()
        return
    for item in [1,2]:
        w(item)
        if (fn()):
            f()
            return
        a(item)
        if (fn()):
            f()
            return
        s(item)
        if (fn()):
            f()
            return
        d(item)
        if (fn()):
            f()
            return
        
