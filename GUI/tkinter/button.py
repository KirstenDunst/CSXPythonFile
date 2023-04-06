'''
Author: Cao Shixin
Date: 2023-03-29 11:11:43
LastEditors: Cao Shixin
LastEditTime: 2023-03-29 11:46:36
Description: 
'''
import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.title('这是一个button demo')
window.geometry('400x300+300+200')


def callback():
    print('按钮被点击')
    messagebox.showinfo(title='温馨提示', message='这是一个info弹窗')


tk.Button(window, text='这是一个按钮', command=callback,
          bg='#7CCD7C', width=20, height=5, activebackground='red', activeforeground='orange').pack()

# 先创建图片对象（如果直接写入buttom的image参数接收里面，加载不出来图片）
btnImg = tk.PhotoImage(
    file='/Users/caoshixin/Person/CSXPythonFile/GUI/tkinter/tk_demo_resources/normal.gif')
tk.Button(window, image=btnImg, command=callback).pack()


window.mainloop()
