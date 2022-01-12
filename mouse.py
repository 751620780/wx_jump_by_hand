#!/usr/bin/python
#-*- coding: utf8 -*-
#python=3.7.0


import win32api
import win32con
import win32gui


def move(x, y):
    """
    函数功能：移动鼠标到指定位置
    参    数：x:x坐标
              y:y坐标
    """
    win32api.SetCursorPos((int(x), int(y)))


def get_cur_pos():
    """
    函数功能：获取当前鼠标坐标
    """
    pos = win32gui.GetCursorPos()
    return pos[0],pos[1]


def left_click():
    """
    函数功能：鼠标左键点击
    """
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def right_click():
    """
    函数功能：鼠标右键点击
    """
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN | win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)


def left_down():
    """
    函数功能：鼠标左键按下
    """
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)


def left_up():
    """
    函数功能：鼠标左键抬起
    """
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def right_down():
    """
    函数功能：鼠标右键按下
    """
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)


def right_up():
    """
    函数功能：鼠标右键抬起
    """
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)