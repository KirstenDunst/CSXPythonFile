'''
Author: Cao Shixin
Date: 2023-03-31 14:34:12
LastEditors: Cao Shixin
LastEditTime: 2023-03-31 14:54:02
Description: 
'''
from tkinter import *
from tkinter import messagebox
import os


window = Tk()
window.title('布局管理方法pack、grid、place')
window.geometry('1200x800+100+100')
window.iconbitmap('')


Label(text='pack堆砌布局').pack()
frame1 = Frame(window)
lb_red = Label(frame1, text="红色", bg="Red", fg='#ffffff', relief=GROOVE)
# 默认以top方式放置
lb_red.pack()
lb_blue = Label(frame1, text="蓝色", bg="blue", fg='#ffffff', relief=GROOVE)
# 沿着水平方向填充，使用 pady 控制蓝色标签与其他标签的上下距离为 5 个像素
lb_blue.pack(fill=X, pady='5px')
lb_green = Label(frame1, text="绿色", bg="green", fg='#ffffff', relief=RAISED)
# 将 黄色标签所在区域都填充为黄色，当使用 fill 参数时，必须设置 expand = 1，否则不能生效
lb_green.pack(side=LEFT, expand=1, fill=BOTH)
frame1.pack()


Label(text='grid网格布局1').pack()
frame2 = Frame(window)
# 在窗口内创建按钮，以表格的形式依次排列
for i in range(10):
    for j in range(10):
        Button(frame2, text=" (" + str(i) + "," + str(j) + ")",
               bg='#D1EEEE') .grid(row=i, column=j)
# 在第5行第11列添加一个Label标签
Label(frame2, text="C语言中文网", fg='blue', font=(
    '楷体', 12, 'bold')).grid(row=4, column=11)
frame2.pack()


Label(text='grid网格布局2').pack()
frame3 = Frame(window)
Label(frame3, text="用户名").grid(row=0, sticky="w")
Label(frame3, text="密码").grid(row=1, sticky="w")
Entry(frame3).grid(row=0, column=1)
Entry(frame3, show="*").grid(row=1, column=1)
# 加载图片LOGO,注意这里是gif格式的图片
photo = PhotoImage(
    file=os.getcwd()+'/tk_demo_resources/normal.gif', width=100, height=80)
Label(frame3, image=photo).grid(
    row=0, column=2, rowspan=2, padx='4px', pady='5px')
# 编写一个简单的回调函数


def login():
    messagebox.showinfo('欢迎来到C语言中文网')


# 使用grid()函数来布局，并控制按钮的显示位置
Button(frame3, text="登录", width=10, command=login).grid(
    row=3, column=0, columnspan=2, sticky="w", padx=10, pady=5)
Button(frame3, text="退出", width=10, command=window.quit).grid(
    row=3, column=1, columnspan=2, sticky="e", padx=10, pady=5)
frame3.pack()


# 创建一个frame窗体对象，用来包裹标签
frame4 = Frame(window, relief=SUNKEN, borderwidth=2, width=450, height=250)
# 在水平、垂直方向上填充窗体
frame4. pack(side=TOP, fill=BOTH, expand=1)
# 创建 "位置1"
Label1 = Label(frame4, text="位置1", bg='blue', fg='white')
# 使用 place,设置第一个标签位于距离窗体左上角的位置（40,40）和其大小（width，height）
# 注意这里（x,y）位置坐标指的是标签左上角的位置（以NW左上角进行绝对定位，默认为NW）
Label1.place(x=40, y=40, width=60, height=50)
# 设置标签2
Label2 = Label(frame4, text="位置2", bg='purple', fg='white')
# 以右上角进行绝对值定位，anchor=NE，第二个标签的位置在距离窗体左上角的(180，80)
Label2.place(x=180, y=80, anchor=NE, width=60, height=30)
# 设置标签3
Label3 = Label(frame4, text="位置3", bg='green', fg='white')
# 设置水平起始位置相对于窗体水平距离的0.6倍，垂直的绝对距离为80，大小为60，30
Label3.place(relx=0.6, y=80, width=60, height=30)
# 设置标签4
Label4 = Label(frame4, text="位置4", bg='gray', fg='white')
# 设置水平起始位置相对于窗体水平距离的0.01倍，垂直的绝对距离为80，并设置高度为窗体高度比例的0.5倍，宽度为80
Label4.place(relx=0.01, y=80, relheight=0.4, width=80)


window.mainloop()
