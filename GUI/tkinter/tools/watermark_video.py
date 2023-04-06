'''
Author: Cao Shixin
Date: 2022-11-16 15:57:44
LastEditors: Cao Shixin
LastEditTime: 2022-11-16 17:59:50
Description: 
'''
import math
import cv2


if __name__ == '__main__':
    video_path = '/Users/caoshixin/Desktop/未命名文件夹/video_1.mp4'
    # input('请输入需要处理的视频路径:')
    save_path = '/Users/caoshixin/Desktop/未命名文件夹'

capture = cv2.VideoCapture('/Users/caoshixin/Desktop/未命名文件夹/output.mp4')
height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
count = capture.get(cv2.CAP_PROP_FRAME_COUNT)
fps = capture.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
outVideo = cv2.VideoWriter()
outVideo.open('/Users/caoshixin/Desktop/未命名文件夹/output_clear.mp4',
              fourcc, fps, (int(width), int(height)), True)


def process_video(image):
    # 需要注意的是第一个范围是y轴坐标的范围,第二个是x轴坐标的范围
    # img=image[1160-90:1160, 509-193:509]
    # img=cv2.GaussianBlur(img,(5,5),1.5)
    # image[1160:1160+90, 509:509+193] = img
    mask = cv2.imread('/Users/caoshixin/Desktop/未命名文件夹/clear.png', 0)
    # new = cv2.imread( '/Users/caoshixin/Desktop/未命名文件夹/avatar_boy.png')
    # 去掉水印
    dst = cv2.inpaint(image, mask, 3, cv2.INPAINT_NS)
    # # 增加新的水印
    # h, w = dst.shape[:2]  # 图片的高度和宽度
    # for i in range(329,h):
    #     for j in range(236,w):
    #         for k in range(3):
    #             dst[i][j][k] =  (int(dst[i][j][k]) + int(new[i][j][k])) if (int(dst[i][j][k]) + int(new[i][j][k]))<255 else 255
    return dst


for i in range(int(count)):
    ret, frame = capture.read()
    if ret is True:
        result = process_video(frame)
        outVideo.write(result)
    else:
        break
    print('进度：', str(math.ceil(i/count*100))+'%')

outVideo.release()
