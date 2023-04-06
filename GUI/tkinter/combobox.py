'''
Author: Cao Shixin
Date: 2023-03-29 19:33:37
LastEditors: Cao Shixin
LastEditTime: 2023-03-29 19:51:41
Description: 
'''
from tkinter import *
from tkinter import ttk

window = Tk()
window.title('这个是ComboBox() demo')
window.geometry('400x250')
window.iconbitmap('')
window.resizable(0, 0)

cbox = ttk.Combobox(window)
cbox.grid(row=1, sticky='NW')
#设置下拉菜单中的值
cbox['value'] = ('C', 'C#', 'C++', 'Python', 'Java')
#设置下拉菜单默认值
cbox.current(3)

# 编写回调函数，执行绑定事件，向文本插入选中文本
def func(event):
    text.insert(INSERT, cbox.get()+'\n')

#绑定下拉菜单事件
cbox.bind('<<ComboboxSelected>>', func=func)
text = Text(window)
text.grid(pady=5)


window.mainloop()
