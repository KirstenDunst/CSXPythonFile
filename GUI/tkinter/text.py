'''
Author: Cao Shixin
Date: 2023-03-29 15:39:15
LastEditors: Cao Shixin
LastEditTime: 2023-03-29 17:28:23
Description: 
'''
from tkinter import *

window = Tk()
window.title('创作一个text demo')
window.geometry('400x420')
window.iconbitmap('')

# 创建一个文本控件
# width：一行可见的字符数，height：显示的行数
text = Text(window, width=50, height=20, undo=True, autoseparators=False)
# 适用 pack(fill=X) 可以设置文本域的填充模式。比如 X表示沿水平方向填充，Y表示沿垂直方向填充，BOTH表示沿水平、垂直方向填充
text.grid()

# INSERT 光标处插入，END 末尾处插入
text.insert(INSERT, '插入内容看看那')
# 继续向后面插入文本
text.insert(
    'insert', ', I Love Python，C语言中文网（网址：c.biancheng.net），一个有温度的网站，一生只做一件事\n\n')


# index文本索引
# 获取字符 ,"1.3"表示第1行第3列，“1.end”：第1行最后一列
print(text.get("1.3", '1.end'))


# 定义撤销和恢复方法
def backout():
    # 撤销
    text.edit_undo()


def regain():
    # 恢复
    text.edit_redo()


Button(window, text='撤销', command=backout).grid(
    row=3, column=0, sticky='w', padx=10, pady=5)
Button(window, text='恢复', command=regain).grid(
    row=3, column=0, sticky='e', padx=10, pady=5)


text.insert(INSERT, '\n\n')
# tag标签
# 在text中插入一个按钮
button = Button(text, text='关闭', command=window.quit)
text.window_create(END, window=button)
# 在第一行文字的第0个字符到第6个字符处插入标签，标签名称为"name"
text.tag_add('name', '1.0', '1.6')
# 将插入的按钮设置其标签名为"button"
text.tag_add('button', button)
# 使用 tag_config() 来改变标签"name"的前景与背景颜色,并加下画线，通过标签控制字符的样式
text.tag_config('name', font=('微软雅黑', 18, 'bold'),
                background='yellow', foreground='blue', underline=1)
# 设置标签"button"的居中排列
text.tag_config('button', justify='center')


# mark文本标记
text.mark_set('标记', '1.end')
# 在标记之后插入相应的文字
text.insert('标记', '<这是通过tag标记插入的内容>')
# 跟着自动移动，往后插入，而不是停留在原位置
text.insert('标记', '《看下mark二次插入的位置》')
# 若使用 mark_unset() 可以删除指定的标记
# text.mark_unset("标记")
# 但使用delete来清楚所有的内容， mark 标记依旧会存在
# text.delete("1.0", "end")
# 依然可以使用 name标记来插入
# text.insert("标记", "Python答疑")


window.mainloop()
