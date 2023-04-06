'''
Author: Cao Shixin
Date: 2023-03-29 13:58:38
LastEditors: Cao Shixin
LastEditTime: 2023-03-29 14:45:59
Description: 
'''
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('这是一个entry页面')
window.geometry('250x100')
window.iconbitmap(
    '/Users/caoshixin/Person/CSXPythonFile/GUI/tkinter/tk_demo_resources/ic_logo.ico')
window.resizable(0, 0)

# entry1 = Entry(window)
# entry1.pack(padx=20, pady=20)
# entry1.delete(0,'end')

# # 插入默认文本
# entry1.insert(0, '插入文本demo')
# # 得到输入框字符串
# print(entry1.get())

# 删除所有字符串
# entry1.delete(0,END)


def check():
    if account_entry.get() == "测试账号":
        messagebox.showinfo(message="输入正确")
        return True
    else:
        messagebox.showerror(message='输入错误')
        account_entry.delete(0, END)
        return False


def reCheck():
    print('reCheck')


def registerCheck(strings, reason, name):
    if pass_entry.get() == '密码':
        messagebox.showinfo(message='密码正确')
        print(strings, reason, name)
        return True
    else:
        messagebox.showerror(message='密码错误')
        pass_entry.delete(0, END)
        print(strings, reason, name)
        return False


Label(window, text='账号：').grid(row=0)
Label(window, text='密码：').grid(row=1)

# 创建动字符串
account_string = StringVar()
account_entry = Entry(window, textvariable=account_string,
                      validate="focusout", validatecommand=check, invalidcommand=reCheck)
account_entry.grid(row=0, column=1)
RegisterTest = window.register(registerCheck)
pass_string = StringVar()
pass_entry = Entry(window, textvariable=pass_string, validate='focusout',
                   validatecommand=(RegisterTest, '%P', '%V', '%W'))
pass_entry.grid(row=1, column=1)


window.mainloop()
