'''
Author: Cao Shixin
Date: 2022-10-26 11:54:07
LastEditors: Cao Shixin
LastEditTime: 2023-03-29 10:12:07
Description: 
'''
from tkinter import *  # 导入tkinter模块【必要步骤】
from tkinter import messagebox

root = Tk()  # 创建主窗口
root.title('一个窗口的标题: caoshixin出品多文本多文本多文本多文本')  # 设置窗口标题
width = 300
height = 200
root.geometry('%dx%d+%d+%d'%(width,height,(root.winfo_screenwidth()-width)/2,(root.winfo_screenheight()-height)/2))  # 设置窗口大小及位置，此处不能为 "*",必须使用 "x"，+横向初始距离(可为负数)+纵向初始距离(可为负数)

# 获取电脑屏幕的大小
print("电脑的分辨率是%dx%d"%(root.winfo_screenwidth(), root.winfo_screenheight()))

#要求窗口的大小，必须先刷新一下屏幕
root.update()
print("窗口的分辨率是%d*%d"%(root.winfo_width(),root.winfo_height()))

# 更改左上角窗口的的icon图标, .icon后缀
root.iconbitmap(
    '/Users/caoshixin/Company/Project/starkid_family/assets/images/avatar_boy.png')

# 如果使窗口不能被拉伸
# root.resizable(0,0)

# 设置主窗口的背景颜色,颜色值可以是英文单词，或者颜色值的16进制数,除此之外还可以使用Tk内置的颜色常量
root["background"] = "#C9C9C9"
root.config(background="#C9C9C9") # background="red"

#设置窗口顶层
root.attributes("-topmost",True)
#设置窗口透明度
root.attributes("-alpha",1)
#设置窗口被调整到最大范围，与resizable()冲突
root.maxsize(600,600)
#设置窗口被调整到最小范围，与resizable()冲突
root.minsize(50,50)

frame = Frame(root, bg='lightgreen')  # 创建一个框架
frame.place(width=200, height=100, x=50, y=50)  # 放置框架
# 这一步骤很关键，不可以直接写成“frame = Frame(root,bg='lightgreen',height=100,width=200).place(width=200,height=100,x=50,y=50)”，不然会报错！
# 创建一个标签控件并赋值给label变量
Label(frame, text='这是一个标签', bg='grey', fg='#F0F0F0', font=(
    '华文新魏', 15), bd=5, relief='groove').pack()  # 为了简化代码，这里就直接放置标签控件

# 添加文本内,设置字体的前景色和背景色，和字体类型、大小
text = Label(root, text="C语言中文网,欢迎您", bg="yellow",
             fg="red", font=('Times', 20, 'bold italic'))
# 将文本内容放置在主窗口内
text.pack()

def callback():
    print("执行回调函数","demodemodemo")
# 添加按钮，以及按钮的文本，并通过command 参数设置关闭窗口的功能
button = Button(root, text="关闭", command=callback)
# 将按钮放置在主窗口内
button.pack(side="bottom")


#定义回调函数，当用户点击X进行退出时，执行用户自定义函数
def QueryWindow():
    #显示一个警告信息，点击确认，销毁窗口
    if messagebox.showwarning("警告","出现了一个错误"):
        # 这里必须使用destory()关闭窗口
        root.destroy()
#是用协议机制与窗口交互，并回调用户自己的函数
root.protocol("WM_DELETE_WINDOW",QueryWindow)

root.mainloop()  # 主窗口进入消息事件循环【必要步骤】
