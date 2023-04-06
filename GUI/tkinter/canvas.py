'''
Author: Cao Shixin
Date: 2023-03-30 14:42:26
LastEditors: Cao Shixin
LastEditTime: 2023-03-30 17:38:42
Description: 
'''
from tkinter import *
import os

window = Tk()
window.title('这是一个Canvas demo')
window.geometry('450x850')
window.iconbitmap('')

Label(window, text='canvas 绘制线:').pack()
cv = Canvas(background='grey', width=300, height=190)
cv.pack()
# 设置坐标点,此处可以元组的形式来设置坐标点
point = [(10, 20), (20, 30), (30, 40), (40, 100), (80, 120), (150, 90)]

# 创建画布，添加线条
# fill 参数指定填充的颜色，如果为空字符串，则表示透明
# dash 参数表示用来绘制虚线轮廓，元组参数，分别代表虚线中线段的长度和线段之间的间隔
# arrow 设线段的箭头样式，默认不带箭头，参数值 first 表示添加箭头带线段开始位置，last表示到末尾占位置，both表示两端均添加
# smooth 布尔值参数，表示是否以曲线的样式划线，默认为 False
# width 控制线宽
line1 = cv.create_line(point, fill='purple', dash=(1, 1), arrow=LAST, width=5)
print('画布line1的id号:', line1)
line2 = cv.create_line(point, fill='red', arrow=BOTH, smooth=TRUE, width=5)
print('线段line2的画布id号:', line2)

# 移动其中一条线段，只需要更改其坐标就可以,使用 coords()方法移动曲线
cv.coords(line2, 50, 30, 25, 35, 35, 40, 50, 120, 60, 170, 10, 180)


Label(window, text='canvas 绘制图形:').pack()

cv1 = Canvas(window, width=400, height=370, bg='white')
# 设置基准坐标
x0, y0, x1, y1 = 10, 10, 80, 80
# 绘制扇形,起始角度为 0 度，结束角度为 270, 扇形区域填充色为淡蓝色，轮廓线为蓝色，线宽为 2px
arc = cv1.create_arc(x0, y0, x1, y1, start=0, extent=270,
                     fill='#B0E0E6', outline='blue', width=2)
# 绘制圆形
oval = cv1.create_oval(x0+150, y0, x1+150, y1,
                       fill='#CD950C', outline='blue', width=2)
# 绘制矩形,并将轮廓线设置为透明色，即不显示最外围的轮廓线，默认为黑色
rect = cv1.create_rectangle(x0, y0+100, x1, y1+100, fill='red', outline='')
# 绘制一个三角形，填充色为绿色
trigon = cv1.create_polygon(
    80, 80, 150, 80, 200, 200, outline='', fill='green')

# 当然也可以绘制一个任意多边形，只要你的坐标正确就可以
# 绘制一个多边形，首先定义一系列的多边形上的坐标点
poly_points = [(0, 280), (140, 200), (140, 240), (270, 240),
               (270, 320), (140, 320), (140, 360)]
polygon = cv1.create_polygon(poly_points, fill="#BF3EFF")

cv1.pack()

Label(window, text='canvas 绘制图片、文本、位图：')
cv2 = Canvas(window, bg='white')
# tkinter 提供的内置位图名称
bitmaps = ["error", "gray75", "gray50", "gray25", "gray12",
           "hourglass", "info", "questhead", "question", "warning"]
# 列出所有的位图样式
for i in range(len(bitmaps)):
    # 前两个参数指定一个位图的位置，后续依次排列
    cv2.create_bitmap((i+1)*30, 30, bitmap=bitmaps[i])
# 并在画布上添加文本
# 参数说明，前两个参数（x0，y0）参照点，指定文字字符串的左上角坐标
# anchor 指定了文本的对于参照点的相对位置，以方位来指定,比如 W/E/N/S等
cv2.create_text(30, 80, text="tkinter内置位图预览", fill='#7CCD7C',
                anchor=W, font=('微软雅黑', 15, 'bold'))
# 定义移动函数


def move_img():
    # 定义移动坐标
    cv2.move(image1, 50, 30)


# 展示图片，使用 PhotoImage()来加载图片
img = PhotoImage(file=os.getcwd() +
                 "/tk_demo_resources/normal.gif", width=300, height=80)
image1 = cv2.create_image(30, 150, image=img, anchor=W)
cv2.create_text(30, 220, text="图片预览", fill='#7CCD7C',
                anchor=W, font=('微软雅黑', 15, 'bold'))
# 将按钮放置在画布中
btn = Button(cv2, text="移动画布", bg="#8A8A8A",
             activebackground="#7CCD7C", command=move_img)
# 在指定位置创建一个窗口控件，tags来添加标签
cv2.create_window(20, 15, height=30, width=40, window=btn)
# 调用delete() 删除画布对象,若传入ALL，则删除所有的画布对象
# cv.delete(image1)
cv2.pack()

window.mainloop()
