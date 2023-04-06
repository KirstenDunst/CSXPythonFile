'''
Author: Cao Shixin
Date: 2023-03-29 11:48:42
LastEditors: Cao Shixin
LastEditTime: 2023-03-29 13:57:43
Description: 
'''
import tkinter as tk
import time

window = tk.Tk()
window.title('这是一个输入框的demo页面')
window.geometry('450x150+100+100')
window.iconbitmap('/Users/caoshixin/Person/CSXPythonFile/GUI/tkinter/tk_demo_resources/ic_logo.ico')
window.resizable(0,0)

#获取时间
def getTime():
    dstr.set(time.strftime("%H:%M:%S"))
    # 间隔1s再次调用
    window.after(1000,getTime)
    
#生成动态字符串
dstr = tk.StringVar()
# 利用textvariable 来实现文本变化
tk.Label(window, textvariable=dstr,fg='green',font=('微软雅黑',85)).pack()

#调用时间生成函数
getTime()

window.mainloop()