'''
Author: Cao Shixin
Date: 2023-03-30 14:25:48
LastEditors: Cao Shixin
LastEditTime: 2023-03-30 14:41:34
Description: 
'''
from tkinter import *

window = Tk()
window.title('这是一个scale控件')
window.geometry('400x350')
window.iconbitmap('')
window.resizable(0, 0)

# 添加一个 Scale 控件，默认垂直方向(orient)，步长设置为 5，长度为200，滑动块的大小为 20，最后使用label参数文本
s1 = Scale(window, from_=100, to=0, resolution=5,
           length=200, sliderlength=20, label='音量控制')
# 设置滑块的位置
s1.set(value=15)
s1.grid()


def scale_select(value):
    label.config(text='您选择的value是:'+value)


s = Scale(window, from_=1, to=100,
          # 设置Scale控件平方向显示
          orient=HORIZONTAL,
          length=400,
          # 设置刻度滑动条的间隔
          tickinterval=9, label='选择你要购买的数量', command=scale_select)
s.grid(row=1)

label = Label(window, text='', font=('微软雅黑', 15, 'bold'), background='#df8943')
label.grid(row=2)


window.mainloop()
