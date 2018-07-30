#! /usr/bin/env python3
# coding='utf-8'

import time
import pyautogui as pag
import os
import win32gui
import win32api

import win32ui

import win32con


def get_point():
    # 采集坐标，并返回w,h,x,y。作为window_capture()函数使用
    try:
        print('正在采集坐标1，请将鼠标移动到光标点')
        #print(3)
        #time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        x1,y1=pag.position() #返回鼠标的坐标
        print('')
        print('采集成功，坐标为：',(x1,y1))
        #time.sleep(2)
        print('正在采集坐标2，请将鼠标移动到光标点')
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        x2,y2=pag.position() #返回鼠标的光标
        print('采集成功，坐标为：',(x2,y2))
        #os.system('cls') #清除屏幕
        w=abs(x2-x1)
        h=abs(y2-y1)
        x=min(x1,x2)
        y=min(y1,y2)
        return(w,h,x,y)
    except  KeyboardInterrupt:
        print('获取失败')


def window_capture(result,filename):
    '''获取截图'''
    #宽度w
    #高度h
    #左上角截图的坐标x,y
    w,h,x,y=result
    hwnd=0
    hwndDC=win32gui.GetWindowDC(hwnd)
    mfcDC=win32ui.CreateDCFromHandle(hwnd)
    saveDC=mfcDC.CreateCompatibleDC()
    saveBitMap=win32ui.CreateBitmap()
    MoniterDev=win32api.EnumDisplayMonitors(None,None)
    #w=MoniterDev[0][2][2]
    # #h=MoniterDev[0][2][3]
    # w=516
    # h=514
    saveBitMap.CreateCompatibleBitmap(mfcDC,w,h)
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0,0),(w,h),mfcDC,(x,y),win32con.SRCOPPY)
    saveBitMap.SaveBitmapFile(saveDC,filename)
