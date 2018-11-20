# coding=utf-8
# author Lingzi time 2018/5/18
#2018/5/20 第一次修改，增加了拷贝部分
#2018/5/26 第二次修改，增加了修改文件夹名称及word创建部分
#2018/6/1  第三次修改，增加autoBlast
#2018/6/12 第四次修改，整合全部内容
#2018/6/16 第五次修改，简化代码，添加注释

import os
import re
import shutil 
import sys
import docx
import time
import webbrowser
import pyautogui

# 输入源文件路径，目标路径
sourcefilepath = ('G:\\Python\\PCR0.0.1\\test')
resultfilepath = ('G:\\Python\\PCR0.0.1\\result')

# 一、源文件处理部分
filenamelist = os.listdir(sourcefilepath)
os.chdir(sourcefilepath)
fnl = []
for i in range(0, len(filenamelist)/2):	# 源文件必须成对出现
    fw = filenamelist[i*2+1]
    fv = fw.split('.', 2)[0] # 采用.号分隔后的第一部分为标识名
    fnl.append(fw)

    # 1.文件夹创建
    os.mkdir(resultfilepath + '\\' + fv) # 以标识名创建文件夹

    # 2.文件拷贝
    for name in filenamelist:
        idname = name.split('.', 2)[0] # 以标识名查找对应文件并复制
        if idname == fv:
            shutil.copyfile(sourcefilepath +'\\'+ name, resultfilepath + '\\' + fv + '\\' + name)

    # 3.Word创建
    st = []
    fword=docx.Document()
    ft = open(fw)
    for line in ft.readlines():
        st.append(line)
    ln = st[0]
    line = ln[50:750]	# word中记录seq文件中的第50个到第750个碱基
    fword.add_paragraph(">"+fv+'\n'+line) 
    fword.save(resultfilepath+'\\'+fv+'\\'+fv+'.docx')

# 二、autoBlast部分
# 以下坐标，间隔时间以及具体内容需根据使用情况更改，具体参考pyautogui的使用手册

for fw in fnl:
    st = []
    ft = open(fw)
    for line in ft.readlines():
        st.append(line)
    ln = st[0]
    line = ln[50:750]
    web = webbrowser.open('https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome')
    time.sleep(10)
    pyautogui.click(70, 500, button='left')
    time.sleep(2)
    pyautogui.typewrite(line)
    time.sleep(2)
    pyautogui.moveTo(1330, 675)
    time.sleep(15)
    pyautogui.click(1330, 675, button='left')
    time.sleep(1)
    pyautogui.moveTo(436, 988)
    time.sleep(1)
    pyautogui.scroll(-1020)
    time.sleep(2)
    pyautogui.click(130, 570, button='left')
    time.sleep(60)
    pyautogui.click(700, 500, button='left')
    time.sleep(0.5)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('s')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('s')
    time.sleep(1)
    wpn = fw.split('.')[0]
    pyautogui.typewrite(wpn)
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.press('enter')

print ("***  Job Done  ***") 
