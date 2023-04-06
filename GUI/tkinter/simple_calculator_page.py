'''
Author: Cao Shixin
Date: 2023-03-29 15:04:12
LastEditors: Cao Shixin
LastEditTime: 2023-03-29 15:12:33
Description: 
'''
from tkinter import *

window = Tk()
window.title('计算器,用于entry组件explain')
window.iconbitmap('')
window.geometry('300x300')

frame = Frame(window)

def calc():
    result = "="+str(eval(expression.get()))
    label.config(text=result)
    
label = Label(frame)
expression = StringVar()
entry = Entry(frame,textvariable=expression)

button = Button(frame,text='等于',command=calc)
#设置Entry控件为焦点所在
entry.focus()
frame.pack()
#Entry控件位于窗体的上方
entry.pack()
#Label控件位于窗体的左方
label.pack(side='left')
#Button控件位于窗体的右方
button.pack(side='right')

frame.mainloop()