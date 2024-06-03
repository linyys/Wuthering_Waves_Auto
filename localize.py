import cv2
import numpy as np
import pyautogui as pg
import keyInput as ki
screen_width, screen_height = pg.size()
def read_img(src):
    img = cv2.imdecode(np.fromfile(src, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    # img = cv2.imread(src, cv2.IMREAD_UNCHANGED)
    # tmpl = cv2.cvtColor(img, cv2.IMREAD_UNCHANGED)
    alpha = img[:, :, 3]
    tmpl = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    return img, alpha, tmpl


def get_local(img, alpha, tmpl):
    screenshot = pg.screenshot()
    s_img = np.array(screenshot)
    gray = cv2.cvtColor(s_img, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(gray, tmpl, cv2.TM_CCORR_NORMED, mask=alpha)
    print(result.max())
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    top_left = max_loc
    h, w = img.shape[:2]
    bottom_right = top_left[0] + w, top_left[1] + h
    return top_left[0] + 7, bottom_right[1] - 7, result.max()

tp_img, tp_alpha, tp_tmpl = read_img("./img/goods/logo2.png")
def tp():
    return get_local(tp_img, tp_alpha, tp_tmpl)


btn_img, btn_alpha, btn_tmpl = read_img("./img/goods/btn.png")
def btn():
    return get_local(btn_img, btn_alpha, btn_tmpl)


option_img, option_alpha, option_tmpl = read_img("./img/goods/option.png")
def option():
    return get_local(option_img, option_alpha, option_tmpl)


card_btn_l_img, card_btn_l_alpha, card_btn_l_tmpl = read_img("./img/goods/card_btn1.png")
card_btn_m_img, card_btn_m_alpha, card_btn_m_tmpl = read_img("./img/goods/card_btn2.png")
def monster_list1():
    l_tl, l_br, _ = get_local(card_btn_l_img, card_btn_l_alpha, card_btn_l_tmpl)
    ki.move_mouse_and_click(l_tl, l_br)
    m_tl, m_br, _ = get_local(card_btn_m_img, card_btn_m_alpha, card_btn_m_tmpl)
    ki.move_mouse_and_click(m_tl, m_br)


card_btn_b_img, card_btn_b_alpha, card_btn_b_tmpl = read_img("./img/goods/card_btn3.png")
def monster_list2():
    l_tl, l_br, _ = get_local(card_btn_l_img, card_btn_l_alpha, card_btn_l_tmpl)
    ki.move_mouse_and_click(l_tl, l_br)
    b_tl, b_br, _ = get_local(card_btn_b_img, card_btn_b_alpha, card_btn_b_tmpl)
    ki.move_mouse_and_click(b_tl, b_br)

def monster(name):
    print("./img/monster/" + name + ".png")
    gw_img, gw_alpha, gw_tmpl = read_img("./img/monster/" + name + ".png")
    tl, br, res = get_local(gw_img, gw_alpha, gw_tmpl)
    if res < 0.98:
        ki.mouse_down()
        return monster(name)
    # if(screen_width == 1920):
    #     return tl + (1200 * 0.75), br - (100 * 0.75)
    # else:
    return tl + 1200, br - 100

resumption_img, resumption__alpha, resumption_tmpl = read_img("./img/goods/resumption.png")
def resumption():
    return get_local(resumption_img, resumption__alpha, resumption_tmpl)


resumption_p_img, resumption_p__alpha, resumption_p_tmpl = read_img(
    "./img/goods/resumption_option.png"
)
def resumption_option():
    return get_local(resumption_p_img, resumption_p__alpha, resumption_p_tmpl)

get_img, get__alpha, get_tmpl = read_img("./img/goods/get_btn.png")
def is_get():
    tl, br, res = get_local(get_img, get__alpha, get_tmpl)
    return (res > 0.95)

open_img, open_alpha, open_tmpl = read_img("./img/goods/open_btn.png")
def is_open():
    tl, br, res = get_local(open_img, open_alpha, open_tmpl)
    return res > 0.95

box_img, box__alpha, box_tmpl = read_img("./img/goods/box.png")
def is_dead():
    tl, br, res = get_local(box_img, box__alpha, box_tmpl)
    return not(res > 0.95)