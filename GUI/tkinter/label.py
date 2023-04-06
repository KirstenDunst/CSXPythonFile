'''
Author: Cao Shixin
Date: 2023-03-29 10:14:44
LastEditors: Cao Shixin
LastEditTime: 2023-03-29 11:10:34
Description: 
'''
from tkinter import *

window = Tk()

window.title("tkinter 学习")
window.geometry('1200x400')
window.config(bg='#8DB6CD')
window.iconbitmap('')

# 若内容是字符则以字符为单位，图像则以像素为单位
label = Label(window, text="这是一个label", font=('宋体', 20, 'bold italic'), bg="#7ccd7c",
              # 设置内容区域大小
              width=30,
              height=5,
              # 设置填充区域距离，边框宽度和其他样式（凹陷式）
              padx=10, pady=15, borderwidth=10, relief="sunken"
              )
# 文字显示再左侧(哪个先放就以那个为主)
label.pack(side='left')

# 显示图片
photo = PhotoImage(
    file='/Users/caoshixin/Person/CSXPythonFile/GUI/tkinter/tk_demo_resources/normal.gif')
print(type(photo))
# 显示在右侧(哪个先放就以那个为主)
lab = Label(window, image=photo).pack(side='right')


#Message同label类似，只不过是添加了自动换行的功能
msg = Message(window,text="这是一个长文本，用来测试换行的效果的，这是一个长文本，用来测试换行的效果的",width=60,font=('微软雅黑',10,'bold'))
msg.pack(side=LEFT)


window.mainloop()
