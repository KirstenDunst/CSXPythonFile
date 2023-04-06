'''
Author: Cao Shixin
Date: 2023-03-31 16:19:07
LastEditors: Cao Shixin
LastEditTime: 2023-03-31 16:45:08
Description: 
'''
from PIL import Image
from tkinter import *
from tkinter import filedialog


window = Tk()
window.title('这是一个filedialog选择图片保存图片的demo')
window.geometry('450x350+300+300')
window.iconbitmap('')


def chooseFile():
    try:
        global img
        file_path = filedialog.askopenfilename()
        fileNameVar.set(file_path)
        img = Image.open(fileNameVar.get())
    except Exception as e:
        print('没有选择任何文件')


def saveFile():
    try:
        filetypes = [("PNG", "*.png"), ("JPG", "*.jpg"), ("GIF",
                                                          "*.gif"), ("txt files", "*.txt"), ('All files', '*')]
        # 返回一个 pathname 文件路径字符串，如果取消或者关闭则返回空字符，返回文件如何操作是后续代码的事情，
        # 该函数知识返回选择文件的文件名字，不具备保存文件的能力
        filenewpath = filedialog.asksaveasfilename(title='保存文件',
                                                   filetypes=filetypes,
                                                   defaultextension='.png',
                                                   initialdir='/Users/caoshixin/Desktop')
        savePathVar.set(filenewpath)
        # 保存文件
        img.save(str(savePathVar.get()))
    except Exception as e:
        print(e)


fileNameVar = StringVar()
savePathVar = StringVar()
Entry(window, textvariable=fileNameVar).grid(row=1, column=0, padx=5, pady=5)
Button(window, text='选择文件', command=chooseFile).grid(
    row=1, column=1, padx=5, pady=5)

Entry(window, textvariable=savePathVar).grid(row=2, column=0, padx=5, pady=5)
Button(window, text='保存文件', command=saveFile).grid(
    row=2, column=1, padx=5, pady=5)


window.mainloop()
