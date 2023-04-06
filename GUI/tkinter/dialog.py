'''
Author: Cao Shixin
Date: 2023-03-31 15:17:04
LastEditors: Cao Shixin
LastEditTime: 2023-03-31 16:17:57
Description: 
'''
from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import messagebox

window = Tk()
window.title('文件选择对话框:filedailog、颜色选择对话框:colorchooser,消息对话框:messagebox')
window.geometry('400x300+200+200')
Label(window, text='文件选择对话框:filedailog').grid()


# 定义一个处理文件的相关函数
def askfile():
    # 从本地选择一个文件，并返回文件的目录
    filename = filedialog.askopenfilename()
    if filename != '':
        lb.config(text=filename)
    else:
        lb.config(text='您没有选择任何文件')


btn = Button(window, text='选择文件', relief=RAISED, command=askfile)
btn.grid(row=1, column=0)
lb = Label(window, text='', bg='#87CEEB')
lb.grid(row=1, column=1, padx=5)


Label(window, text='颜色选择对话框:colorchooser', bg='red').grid(row=5)


def colorSelct():
    colorValue = colorchooser.askcolor()
    colorLabel.config(text='颜色值：'+str(colorValue))


colorLabel = Label(window, font=('宋体', 15), text='')
colorLabel.grid(row=6)
Button(window, text='点击选择颜色', bg='#9AC0CD', command=colorSelct).grid(row=7)


Label(window, text='消息对话框:messagebox').grid(row=10)


def messageBtnChoose():
    messagebox.askokcancel('提示', '你确定要关闭么？')


Button(window, text='message dialog按钮',
       command=messageBtnChoose, bg='#da3425').grid(row=11)


window.mainloop()
