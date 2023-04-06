'''
Author: Cao Shixin
Date: 2023-03-30 13:56:58
LastEditors: Cao Shixin
LastEditTime: 2023-03-30 14:23:07
Description: 
'''
from tkinter import *

window = Tk()
window.geometry('500x200')
window.title('这是一个CheckButton demo')
window.iconbitmap('')
window.resizable(0, 0)

Label(window, text='c语言中文培训班', font=('微软雅黑', 18, 'bold'), fg='#cd7054').pack()

# 创建int参数变量
checkVar1 = IntVar()
checkVar2 = IntVar()
checkVar3 = IntVar()
check1 = Checkbutton(window, text='Python', variable=checkVar1,
                     onvalue=1, offvalue=0, font=('微软雅黑', 15, 'bold'))
check2 = Checkbutton(window, text='Java', variable=checkVar2,
                     onvalue=1, offvalue=0, font=('微软雅黑', 15, 'bold'))
check3 = Checkbutton(window, text='C语言', variable=checkVar3,
                     onvalue=1, offvalue=0, font=('微软雅黑', 15, 'bold'))
# 做默认选中
check1.select()
# 取消选中(注意和deselect()区分)
check1.toggle()

check1.pack(side=LEFT)
check2.pack(side=LEFT)
check3.pack(side=LEFT)


def study():
    if checkVar1.get() == 0 and checkVar2.get() == 0 and checkVar3.get() == 0:
        s = '你还没有选择任何一个'
    else:
        s1 = 'Python' if (checkVar1.get() == 1) else ''
        s2 = 'Java' if (checkVar2.get() == 1) else ''
        s3 = 'C语言' if (checkVar3.get() == 1) else ''
        s = '您选择了%s %s %s' % (s1, s2, s3)
    label.config(text=s)


Button(window, text='选好了', background='#bebebe',
       command=study).pack(side=LEFT)

label = Label(window, text='', font=('微软雅黑', 15, 'bold'),
              background='#983472', width=5, height=2)
label.pack(side=BOTTOM, fill=X)


window.mainloop()
