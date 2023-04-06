'''
Author: Cao Shixin
Date: 2023-03-31 14:55:23
LastEditors: Cao Shixin
LastEditTime: 2023-03-31 15:14:26
Description: 
'''
from tkinter import *

window1 = Tk()
window1.geometry('450x350+200+200')
window1.title('布局管理控件:Frame, LabelFrame, PanedWindow, TopLevel')

Label(text='Frame控件').pack()
# 在主窗口上添加一个frame控件
frame1 = Frame(window1)
frame1.pack()
# 在frame_1上添加另外两个frame， 一个在靠左，一个靠右
# 左侧的frame
frame_left = Frame(frame1)
Label(frame_left, text='左侧标签1', bg='green',
      width=10, height=5).grid(row=0, column=0)
Label(frame_left, text='左侧标签2', bg='blue',
      width=10, height=5).grid(row=1, column=1)
frame_left.pack(side=LEFT)
frame_right = Frame(frame1)
Label(frame_right, text='右侧标签1', bg='gray',
      width=10, height=5).grid(row=0, column=1)
Label(frame_right, text='右侧标签2', bg='pink',
      width=10, height=5).grid(row=1, column=0)
Label(frame_right, text='右侧标签3', bg='purple',
      width=10, height=5).grid(row=1, column=1)
frame_right.pack(side=RIGHT)
window1.mainloop()


window2 = Tk()
window2.geometry('450x350+200+200')
window2.title('布局管理控件:Frame, LabelFrame, PanedWindow, TopLevel')
Label(text='LabelFrame控件,拖动整体大小改变下试试看').pack()
# 定义第一个容器，使用 labelanchor ='w' 来设置标题的方位
frame_left = LabelFrame(window2, text="教程", labelanchor="w", bg='#5CACEE')
# 使用 place 控制 LabelFrame 的位置
frame_left.place(relx=0.2, rely=0.2, relwidth=0.2, relheight=0.5)
label_1 = Label(frame_left, text="C语言")
label_1.place(relx=0.2, rely=0.2)
label_2 = Label(frame_left, text="Python")
label_2.place(relx=0.6, rely=0.2)
label_3 = Label(frame_left, text="Java")
label_3.place(relx=0.2, rely=0.6)
label_4 = Label(frame_left, text="C++")
label_4.place(relx=0.6, rely=0.6)
# 定义第二个容器，使用 labelanchor ='w' 来设置标题的方位
frame_right = LabelFrame(window2, text="辅导班", labelanchor="w", bg='#66CDAA')
# 使用 place 控制 LabelFrame 的位置
frame_right.place(relx=0.5, rely=0.2, relwidth=0.3, relheight=0.6)
label_1 = Label(frame_right, text="C语言辅导班")
label_1.place(relx=0.2, rely=0.2)
label_2 = Label(frame_right, text="数据结构")
label_2.place(relx=0.6, rely=0.2)
label_3 = Label(frame_right, text="C++辅导班")
label_3.place(relx=0.2, rely=0.6)
label_4 = Label(frame_right, text="Python答疑")
label_4.place(relx=0.6, rely=0.6)

window2.mainloop()


window3 = Tk()
window3.geometry('450x350+200+200')
window3.title('布局管理控件:Frame, LabelFrame, PanedWindow, TopLevel')
Label(text='PanedWindow控件,改变整体大小,拖动中间分割线').pack()
# 创建一个水平方向的 panedwindow，并添加到主窗口中，默认为水平方向
p_window1 = PanedWindow(window3)
p_window1.pack(fill=BOTH, expand=1)
# 在窗口区的左侧添加两个水平方向的 Label
left1 = Label(p_window1, text='C语言中文网', bg='#7CCD7C',
              width=10, font=('微软雅黑', 15))
p_window1.add(left1)
left2 = Label(p_window1, text='网址:c.biancheng.net',
              bg='#9AC0CD', width=10, font=('微软雅黑', 15))
p_window1.add(left2)
# 创建一个垂直方向的panedwindow,并添加一个手柄，设置分割线样式
p_window2 = PanedWindow(orient=VERTICAL, showhandle=True, sashrelief='sunken')
# 添加到 p_window1中
p_window1.add(p_window2)
# 在 p_window2 中添加两个垂直方向的标签
top_label = Label(p_window2, text='教程', bg='#7171C6',
                  height=8, font=('宋体', 15))
p_window2.add(top_label)
bottom_label = Label(p_window2, text='辅导班', bg='#8968CD', font=('宋体', 15))
p_window2.add(bottom_label)

window3.mainloop()


window4 = Tk()
window4.geometry('450x350+200+200')
window4.title('布局管理控件:Frame, LabelFrame, PanedWindow, TopLevel')
Label(text='Toplevel控件').pack()


def create_toplevel():
    top = Toplevel()
    top.title("C语言中文网")
    top.geometry('300x200+100+100')
    top.iconbitmap('')
    # 多行文本显示Message控件
    msg = Label(top, text="网址:c.biancheng.net", bg='#9BCD9B', font=('宋体', 15))
    msg.pack()


Button(window4, text="点击创建Toplevel组件", width=20,
       height=3, command=create_toplevel).pack()
window4.mainloop()
