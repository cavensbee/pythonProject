#! /usr/bin/env python3
# coding:utf-8

import os,time
import pyautogui as pag
import win32gui
import win32api,win32ui,win32con,win32gui
from PIL import Image
import pytesseract
import webbrowser
#获取sdk http://ai.baidu.com/
#获取aip pip install git+https://github.com/Baidu-AIP/python-sdk.git@master
from aip import AipOcr
import json
status=0
""" 你的 APPID AK SK """
APP_ID='****'
API_KEY='***'
SECRET_KEY='***'
client=AipOcr(APP_ID,API_KEY,SECRET_KEY)
""" 读取图片 """

def get_question(path):
    '''百度识别图片文字'''
    with open(path,'rb') as fp:
        image=fp.read()
    res=client.basicGeneral(image)
    words=res['words_result']
    lines=[item['words'] for item in words]
    question=''.join(lines)
    if question[1]=='.':
        question=question[2:]
    elif question[2]=='.':
        question=question[3:]
    return question.replace('?',' ')

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
    saveDC.BitBlt((0,0),(w,h),mfcDC,(x,y),win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC,filename)

def get_point_txt(status):
    #如果status=y，则重新获取坐标
    '''如果存在point.txt，则询问是否重新采集，删除point.txt;如果不存在point.txt,则直接采集'''
    if not os.path.isfile('point.txt'):
        result=get_point()
        with open('point.txt','w') as f:
            f.write(str(result))
        return result
    else:
        if status=='y':
            result=get_point()
            with open('point.txt','w') as f:
                f.write(str(result))
            return result
        else:
            with open('point.txt','r') as f:
                result=f.readline()
            result=eval(result)
            return result

def orc_pic():
    #识别中文
    text=pytesseract.image_to_string(Image.open('jietu.jpg'),lang='chi_sim')
    #识别英文
    # text=pytesseract.image_to_string(Image.open('jietu.jpg'))
    text=''.join(text.split())
    return text

#百度识别
def orc_baidu():
    text=get_question('jietu.jpg')
    return text

status='y'
start=time.time()
result=get_point_txt(status)
for i in range(10):
    window_capture(result,'jietu.jpg')
#text=orc_baidu()
text=orc_pic()
print(text)

#浏览器搜索
url='http://www.baidu.com/s?wd=%s' % text
webbrowser.open(url)
end=time.time()
time=end-start
print('此次耗时%.lf秒' % time)

input("Enter the any press to exit")