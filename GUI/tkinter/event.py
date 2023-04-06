'''
Author: Cao Shixin
Date: 2023-03-31 13:55:04
LastEditors: Cao Shixin
LastEditTime: 2023-03-31 14:27:44
Description: 
'''
from tkinter import *

window = Tk()
window.title('这是一个Event事件处理')
window.geometry('450x350+200+100')
window.iconbitmap('')


def show_key(event):
    # 查看触发事件的按钮
    s = event.keysym
    # 将其显示在控件上
    lb.config(text=s)


lb = Label(window, text='请按键', font=('微软雅黑', 15), fg='blue')
# 给按钮添加绑定事件
lb.bind('<Key>', show_key)
# 设置按钮获取焦点 (只有获取焦点才能接受键盘事件)
lb.focus_set()
lb.pack()


window.mainloop()


def handleMotion(event):
    label1.config(text='你移动了光标的所在位置')
    label2['text'] = '目前光标位置: x=%d,y=%d' % (event.x, event.y)
    print('光标当前的位置：', event.x, event.y)


window2 = Tk()
window2.title('鼠标事件')
window2.geometry('450x350+400+200')
window2.iconbitmap('')

frame = Frame(window2, relief=RAISED, borderwidth=2, width=300, height=200)
frame.bind('<Motion>', handleMotion)
label1 = Label(frame, text='没有任何点击', bg='purple')
label1.place(x=20, y=20)
label2 = Label(frame, text='')
label2.place(x=16, y=60)

frame.pack(side=TOP)

window2.mainloop()
