'''
Author: Cao Shixin
Date: 2023-03-31 11:41:59
LastEditors: Cao Shixin
LastEditTime: 2023-03-31 13:54:17
Description: 
'''
from tkinter import *

window = Tk()
window.title('这是一个scrollbar 的demo')
window.geometry('450x180+300+200')
window.iconbitmap('')

sbar1 = Scrollbar(window)
sbar1.pack(side=RIGHT, fill=Y)
sbar2 = Scrollbar(window, orient=HORIZONTAL)
sbar2.pack(side=BOTTOM, fill=X)

mylist = Listbox(window, xscrollcommand=sbar2.set, yscrollcommand=sbar1.set)
for i in range(30):
    mylist.insert(
        END, '第%d次,猜猜看,横向扩展扩展，看可滑动，横向扩展扩展，看可滑动，横向扩展扩展，看可滑动，横向扩展扩展，看可滑动' % (i+1))
mylist.pack(side=LEFT, fill=BOTH)
sbar1.config(command=mylist.yview)
sbar2.config(command=mylist.xview)


window.mainloop()
