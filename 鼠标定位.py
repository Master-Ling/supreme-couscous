# coding=utf-8
# author Lingzi time 2018/6/16


import pyautogui

for x in range(0,100):
    i=input()
    if i==1:
        x,y=pyautogui.position()
        print x,y
    else:
        exit()