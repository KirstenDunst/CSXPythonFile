'''
Author: Cao Shixin
Date: 2023-03-29 15:15:27
LastEditors: Cao Shixin
LastEditTime: 2023-03-29 15:21:13
Description: 
'''
from tkinter import *

window = Tk()
window.title('自带选择且可输入组件Spinbox demo')
window.geometry('300x200+300+200')
window.iconbitmap('')

Spinbox(window, from_=0, to=20, increment=2, width=15, bg='#9BCD9B').pack()

Entry(window).pack()

Spinbox(window,values=('Python','Java','c','c#','php')).pack()


window.mainloop()
