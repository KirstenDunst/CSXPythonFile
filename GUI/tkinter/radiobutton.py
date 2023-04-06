'''
Author: Cao Shixin
Date: 2023-03-30 11:32:31
LastEditors: Cao Shixin
LastEditTime: 2023-03-30 13:53:45
Description: 
'''

from tkinter import *

window = Tk()
window.title('这是一个单选框RadioButton()组件的demo')
window.geometry('400x180')
window.iconbitmap('')

v = IntVar()
v.set(0)

for name, num in [('选项1', 1), ('选项2', 2), ('选项3', 3), ('选项4', 4)]:
    Radiobutton(window, text=name, variable=v, value=num).pack(anchor='w')


def select():
    string = '您选择了'+dist.get(v1.get())+',祝你学习愉快'
    label.config(text=string)


dist = {1: '中文网', 2: '菜鸟教程', 3: 'w3cschool', 4: '微学苑'}

label = Label(window, font=('微软雅黑', 12, 'bold'), fg='#43cd80')
label.pack(side=BOTTOM)
v1 = IntVar()
for key, value in dist.items():
    Radiobutton(value=key, variable=v1, text=value,
                command=select, indicatoron=False).pack(anchor='w')


window.mainloop()
