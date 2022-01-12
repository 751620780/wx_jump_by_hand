#!/usr/bin/python
#-*- coding: utf8 -*-
#python=3.7.0

import os
import sys
import time
import mouse
import random
import win32gui
import cv2
from PIL import ImageGrab
import numpy as np

rat=0.0

def random_x(x0):
    x1 = int(x0 + random.randint(-5, 5) * 10)
    if x1 > xe: x1 = xe - 100
    return x1


def random_y(y0):
    y1 = int(y0 + random.randint(-5, 5) * 10)
    if y1 > ye: y1 = ye - 100
    return y1


def jump(distance, x, y):
    """第一跳像素距离是530px，大约0.72秒"""
    press_time = float(distance) * 1.35 * 0.001  # ms
    mouse.move(random_x(x), random_y(y))
    mouse.left_down()
    time.sleep(press_time)
    mouse.left_up()
    time.sleep(random.randint(6, 10) * 0.2)


def get_wx_jump_window_area():
    """获取微信跳一跳程序的窗口区域"""
    try:
        hwnd = win32gui.FindWindow(None, "跳一跳")
        x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
        # win32gui.EnableWindow(hwnd)
        return x0, y0, x1, y1
    except:
        print("你开启了电脑版的微信小程序跳一跳游戏了吗？")
        sys.exit(-1)


def snap_wx_jump_window_area():
    """截取微信跳一跳程序的窗口区域"""
    bbox = (xs, ys, xe, ye)
    img = ImageGrab.grab(bbox)
    img.save("main_window.jpg")
    img.getpixel


def get_button_position():
    """获得游戏开始按钮的位置"""
    def get_start_button_position():
        img = cv2.imread("main_window.jpg")
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        template = cv2.imread("start.png", 0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            # xs是基准点，ys是基准点
            return pt[0] + w / 2 + xs + 10, pt[1] + h / 2 + ys + 10
        return 0, 0

    def get_restart_button_position():
        img = cv2.imread("main_window.jpg")
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        template = cv2.imread("restart.png", 0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            # xs是基准点，ys是基准点
            return pt[0] + w / 2 + xs + 10, pt[1] + h / 2 + ys + 10
        return 0, 0

    x, y = get_start_button_position()
    if x == 0: x, y = get_restart_button_position()
    return x, y


def get_you_position():
    """获取微信跳一跳程序中的“你”的位置"""
    img = cv2.imread("main_window.jpg")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread("you.png", 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        # xs是基准点，ys是基准点，90像素是向下偏移90，因为截取图像是头部
        return pt[0] + w / 2 + xs, pt[1] + h / 2 + ys + 90




def get_next_position():
    """
        获取微信跳一跳程序中的小人要跳“下一个”的位置屏幕坐标位置
        查找原理：下一个平台的位置只会在屏幕的1/3~1/2之间，先自上向下自左向右的扫描点的颜色不同于之前的点，此点的x坐标记为目标x，
                  记录此点的颜色，然后从右往左扫自上向下扫找到第一个颜色相同的点的纵坐标为目标的y
        
    """
    px=0
    py=0
    value=0
    img = cv2.imread("main_window.jpg")
    cv2.imshow("Image", img)
    time.sleep(1.0)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Image", img_gray)
    time.sleep(1.0)
    # y_start=int(int(ye-ys) / 3)
    # y_end =int(int(ye-ys) / 2)
    # for i in range(y_start,y_end):
    #     for j in range(15,xe-xs):
    #         print(img_gray[j][i],end="")
    #         print(" ",end="")
    #     print()
    # print(px,value)
    # for i in range(y_start,y_end):
    #     for j in range(15,xe-xs):
    #         if img_gray[j][i] != img_gray[j-1][i]:
    #             px=j
    #             value=img_gray[j][i]
    #             break
    # print(px,value)
            
                



def cal_distance(x0, y0, x1, y1):
    """
        由于电脑的显示比例放大问题，可能在每一台设备的距离不一样，这里需要归一化
        第一次的像素距离*比例=530
    """
    global rat
    d=((x1 - x0)**2 + (y1 - y0)**2)**0.5
    if rat<=0.0001:
        rat=530/d
        print("rat=",rat)
        return 530
    else:
        return d*rat


xs, ys, xe, ye = get_wx_jump_window_area()

if __name__ == "__main__":
    time.sleep(1)
    # 移动鼠标到窗口中央附近
    mouse.move(random_x((xs + xe) / 2), random_y((ys + ye) / 2))
    # 获取当前鼠标位置
    x0, y0 = mouse.get_cur_pos()
    # 窗口截图
    snap_wx_jump_window_area()
    xst, yst = get_button_position()
    if xst != 0:
        print("开始按钮位置：",xst-xs, yst-ys)
        mouse.move(xst, yst)
        mouse.left_click()
        time.sleep(1)
    while True:
        snap_wx_jump_window_area()
        xyou, yyou = get_you_position()
        print("人物初始位置：",xyou-xs, yyou-ys)
        xnext, ynext = get_next_position()
        print("跳跃从({},{})到({},{})".format(xyou-xs, yyou-ys, xnext-xs, ynext-ys))
        distance = cal_distance(xyou, yyou, xnext, ynext)
        jump(distance, x0, y0)
        time.sleep(0.5)

# if __name__ == "__main__":
#     # snap_wx_jump_window_area()
#     get_next_position()