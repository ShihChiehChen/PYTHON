#檢查outlook.pst檔的容量
#
#
#

from tkinter import *
#import tkinter as tk

from pathlib import Path

from my_module import *


# 這是單行註解
""" i這是多行註解 """

path = 'D:\\20210118-1_full_b1_s1_v1.tib'
file=Path('D:\\20210118-1_full_b1_s1_v1.tib')

#設定標籤的提示訊息
# message=fileExist(path)
if file.exists():
    filesize=toGetFilesize(path)
    volume=str(filesize).split('.')
    integer=volume[0]
    decimal=volume[1][0:2]
    filesizeMessage="您的PST檔容量為："+integer+"."+decimal+"GB。\n\n"
    tipMessage=toGetMessage(filesize)
    message=filesizeMessage+tipMessage
else:
    message='檔案不存在。'


#設定標籤文字
fontcolor=setfontcolor(filesize)

#設定視窗
win = Tk()                          # 建立主視窗物件
win.resizable(False,False)             # 設定主視窗的寬跟高皆不可縮放
win.title('This is python GUI practice.')  # 設定主視窗標題
#win.iconbitmap('YouTube.ico') #設定視窗 icon
lb=Label(win,width="40",height="10")
lb.config(text=message)
lb.config(fg=fontcolor)
lb.config(font=('Arial',16,'bold'))
lb.pack()

#啟動主視窗
win.mainloop()
