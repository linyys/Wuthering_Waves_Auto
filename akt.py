import pyautogui as pg
import time
import yaml


def p():
    pg.click(clicks=6, interval=0.3, duration=0, button="left")

def long_p():
    pg.mouseDown(button='left')
    time.sleep(1)
    pg.mouseUp(button='left')

def e_akt():
    pg.press("e", presses=1, interval=0.3)

def r():
    pg.press("r", presses=1, interval=0.3)

def shift():
    pg.keyDown('w')
    pg.click(clicks=1, interval=0.2, duration=0, button="right")
    time.sleep(0.2)
    pg.keyUp('w')

def q():
    pg.keyDown('q')
    pg.keyUp('q')

def latch():
    pg.click(clicks=1, interval=0.3, duration=0, button="middle")
who = 1
def change():
    global who
    if (who >= 3):
        who = 1
    pg.press(str(who), presses=1, interval=0.3)
    who += 1

def read_config():
    print(akt_list)
with open('./config.yaml', 'r', encoding='utf-8') as f:
    result = yaml.load(f.read(), Loader=yaml.FullLoader)
akt_index = 0
akt_list = result['akt']
def akt_main():
    global akt_index
    global akt_list
    if (akt_index >= len(akt_list)):
        akt_index = 0
    fn = akt_list[akt_index]
    exec('{}'.format(fn))
    akt_index += 1