'''
Author: Cao Shixin
Date: 2023-03-29 11:41:50
LastEditors: Cao Shixin
LastEditTime: 2023-03-29 11:43:51
Description: 
'''
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('这是一个登录UI页面')
window.geometry('400x200+100+100')
window.resizable(0, 0)


# grid()网格型布局
# 将两个标签分别布置在第一行第二行开头
tk.Label(window, text='账号:').grid(row=0)
tk.Label(window, text='密码:').grid(row=1)
# 创建输入框组件
e1 = tk.Entry(window)
e2 = tk.Entry(window, show='*')  # 以*的形式显示密码
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)


def login():
    messagebox.showinfo('欢迎你的到来')


tk.Button(window, command=login, width=10, text='登录').grid(
    row=3, column=0, sticky='w', padx=10, pady=5)
tk.Button(window, command=window.quit, width=10, text='退出').grid(
    row=3, column=1, sticky='e', padx=10, pady=5)


window.mainloop()
