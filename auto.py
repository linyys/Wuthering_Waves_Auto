import keyInput as ki
import akt
import localize
import time
def change_map():
    ki.open_map()
    ki.scroll(-30)
    ki.scroll(15)
    ki.open_map()

def search_resumption():
    while True:
        tl, br, res = localize.resumption()
        if res > 0.98:
            ki.move_mouse_and_click(tl, br)
            break
        else:
            ki.open_map()
            ki.open_map()

timeout = 90
def go(monster_uid):
    time.sleep(3)
    ki.open_card()
    if monster_uid == "10" or monster_uid == "11":
        localize.monster_list2()
    else:
        localize.monster_list1()
    tl, br = localize.monster(monster_uid)
    ki.move_mouse_and_click(tl, br)
    time.sleep(2)
    ki.esc()
    ki.move_mouse_and_click(localize.screen_width / 2, localize.screen_height / 2)
    tl, br, _ = localize.option()
    ki.move_mouse_and_click(tl, br)
    tl, br, _ = localize.btn()
    ki.move_mouse_and_click(tl, br)
    if monster_uid == "11":
        time.sleep(18)
    else:
        time.sleep(8)
    if monster_uid == "5":
        ki.search(localize.is_open)
        time.sleep(8)
    akt.p_akt()
    time.sleep(0.6)
    akt.latch()
    now_time = time.time()
    while localize.is_dead():
        if time.time() - now_time > timeout:
            break
        akt.akt_main()
        time.sleep(1)
        if localize.is_get():
            ki.f()
        else:
            ki.search(localize.is_get)
        ki.open_map()
        search_resumption()
        tl, br, res = localize.resumption_option()
        if res > 0.95:
            ki.move_mouse_and_click(tl, br)
        tl, br, _ = localize.btn()
        ki.move_mouse_and_click(tl, br)