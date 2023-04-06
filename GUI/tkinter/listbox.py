'''
Author: Cao Shixin
Date: 2023-03-29 17:30:03
LastEditors: Cao Shixin
LastEditTime: 2023-03-29 19:32:27
Description: 
'''
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('这是一个列表框demo')
window.geometry('400x200')
window.iconbitmap('')

listbox = Listbox(window)
listbox.pack()

for i, item in enumerate(['c', 'c++', 'c#', 'java', 'php', 'python']):
    listbox.insert(i, item)

# 同样的循环也可以写成下面这样
for item in ['c', 'c++', 'c#', 'java', 'php', 'python']:
    listbox.insert('end', item)


# 增加滚动条和删除功能
# 滚动条
s = Scrollbar(window)
# 设置垂直滚动条显示的位置，使得滚动条，靠右侧；通过 fill 沿着 Y 轴填充
s.pack(side=RIGHT, fill=Y)
# 将 selectmode 设置为多选模式，并为Listbox控件添加滚动条
listbox1 = Listbox(window, selectmode=MULTIPLE, height=5, yscrollcommand=s.set)
for i, item in enumerate(range(1, 50)):
    listbox1.insert(i, item)
listbox1.pack()

# 设置滚动条，使用 yview使其在垂直方向上滚动 Listbox 组件的内容，通过绑定 Scollbar 组件的 command 参数实现
s.config(command=listbox1.yview)

# 使用匿名函数,创建删除函数，点击删除按钮，会删除选项
Button(window, text='删除', command=lambda x=listbox1: x.delete(
    ACTIVE)).pack(pady=10)


# StringVar()添加列表选项
var1 = StringVar()
Label(window, bg='#b0b0b0', font=('微软雅黑', 15),
      width=20, textvariable=var1).pack()

def click_button():
    try:
        val = lb.get(lb.curselection())
        var1.set(val)
    except Exception as e:
        messagebox.showerror(title='发现一个错误', message='没有选择任何条目')


Button(window, text='获取当前选项', command=click_button).pack()

var2 = StringVar()
var2.set(('C语言辅导班', "Python答疑辅导", "Java答疑辅导", "C++辅导"))
lb = Listbox(window, listvariable=var2)
for item in ["C", "Java", "Python", "C#", "Golang", "Runby"]:
    lb.insert('end', item)
lb.insert(0, '编程学习')
lb.delete(4)
lb.pack()

window.mainloop()
