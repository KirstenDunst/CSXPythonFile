'''
Author: Cao Shixin
Date: 2023-03-30 17:39:39
LastEditors: Cao Shixin
LastEditTime: 2023-03-31 14:33:01
Description: 
'''
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('这是一个menu demo')
window.geometry('450x350+300+200')
window.iconbitmap('')


def menuCommand():
    messagebox.showinfo(message='这是一个菜单点击')


main_menu = Menu(window)
# mac osx不允许你直接把命令放在主菜单上，在主菜单上只能添加级连
filemenu = Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="文件", menu=filemenu)
filemenu.add_command(label='文件操作1', command=menuCommand, accelerator='Ctrl+N')
filemenu.add_command(label='文件操作2', command=menuCommand, accelerator='Ctrl+O')
filemenu.add_command(label='文件操作3', command=menuCommand, accelerator='Ctrl+S')
filemenu.add_separator()
filemenu.add_command(label='退出', command=window.quit)
editmenu = Menu(main_menu)
main_menu.add_cascade(label='编辑', menu=editmenu)
editmenu.add_command(label='编辑1', command=menuCommand)
editmenu.add_command(label='编辑2', command=menuCommand)
editmenu.add_command(label='编辑3', command=menuCommand)
factorymenu = Menu(main_menu)
main_menu.add_cascade(label='格式', menu=factorymenu)
factorymenu.add_command(label='格式1', command=menuCommand)
factorymenu.add_command(label='格式2', command=menuCommand)
factorymenu.add_command(label='格式3', command=menuCommand)
checkmenu = Menu(main_menu)
main_menu.add_cascade(label='查看', menu=checkmenu)
checkmenu.add_command(label='查看1', command=menuCommand)
checkmenu.add_command(label='查看2', command=menuCommand)
checkmenu.add_command(label='查看3', command=menuCommand)


menubtn = Menubutton(window, text='点我进行操作', relief='sunken')
menubtn.grid(padx=195, pady=105)
helpmenu = Menu(menubtn, tearoff=False)
helpmenu.add_command(label='帮助1')
helpmenu.add_command(label='帮助2')
helpmenu.add_command(label='帮助3')
# 显示菜单，将菜单命令绑定在菜单按钮对象上
menubtn.config(menu=helpmenu)


# 绑定键盘事件，按下键盘上的相应的键时都会触发执行函数
window.bind("<Control-n>", lambda event: menuCommand())
window.bind("<Control-N>", lambda event: menuCommand())
window.bind("<Control-o>", lambda event: menuCommand())
window.bind("<Control-O>", lambda event: menuCommand())
window.bind("<Control-s>", lambda event: menuCommand())
window.bind("<Control-S>", lambda event: menuCommand())

window.config(menu=main_menu)
window.mainloop()


window2 = Tk()
window2.title('右键显示菜单(mac上面暂时无效)')
window2.geometry('450x350+200+200')


def func():
    print('您通过弹出菜单执行了命令')


# 创建一个弹出菜单
menu = Menu(window2, tearoff=False)
menu.add_command(label="新建", command=func)
menu.add_command(label="复制", command=func)
menu.add_command(label="粘贴", command=func)
menu.add_command(label="剪切", command=func)


# 定义事件函数
def command(event):
    # 使用 post()在指定的位置显示弹出菜单
    menu.post(event.x_root, event.y_root)


# 绑定鼠标右键，这是鼠标绑定事件
# <Button-3>表示点击鼠标的右键，1 表示左键，2表示点击中间的滑轮
window2.bind("<Button-3>", command)

window2.mainloop()
