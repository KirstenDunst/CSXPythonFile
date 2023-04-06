'''
Author: Cao Shixin
Date: 2023-03-31 16:50:46
LastEditors: Cao Shixin
LastEditTime: 2023-03-31 17:10:22
Description: 
'''
from tkinter import *
from time import strftime

window = Tk()
window.title('演示一个时钟demo')
window.geometry('450x350+300+300')
window.iconbitmap('')

lb = Label(window, font=('微软雅黑', 50, 'bold'), bg='#fd4567', fg='#23569e')
lb.pack(anchor='center', fill=BOTH, expand=1)

mode = 'time'


def showTime():
    str = strftime('%H:%M:%S %p') if mode == 'time' else strftime('%Y-%m-%d')
    lb.config(text=str)
    lb.after(1000, showTime)


def mouseClick(event):
    global mode
    mode = 'date' if mode == 'time' else 'time'


lb.bind('<Button>', mouseClick)

showTime()

window.mainloop()
