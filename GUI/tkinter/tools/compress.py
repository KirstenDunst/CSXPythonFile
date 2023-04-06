'''
Author: Cao Shixin
Date: 2022-11-15 15:34:39
LastEditors: Cao Shixin
LastEditTime: 2023-04-04 10:14:39
Description: 
'''
import os
import shutil
import threading
import cv2
from ffmpy3 import FFmpeg
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


def select_file():
    # 单个文件选择
    selected_file_path = filedialog.askopenfilename()  # 使用askopenfilename函数选择单个文件
    select_path.set(selected_file_path)


def select_files():
    # 多个文件选择
    selected_files_path = filedialog.askopenfilenames()  # askopenfilenames函数选择多个文件
    select_path.set('\n'.join(selected_files_path))  # 多个文件的路径用换行符隔开


def select_folder():
    # 文件夹选择
    selected_folder = filedialog.askdirectory()  # 使用askdirectory函数选择文件夹
    select_path.set(selected_folder)


def compress():
    log_string.set('开始执行压缩转换')
    path = select_path.get()
    if os.path.exists(path):
        # 文件执行or文件夹执行
        newDirName = 'after_compress'
        new_path = path + '/'+newDirName
        if os.path.exists(new_path):
            result = messagebox.askokcancel("提示已存在after_compress文件夹","是否覆盖以继续？")
            if(result == True):
                shutil.rmtree(new_path)
            else :
                log_string.set('操作结束')
                return
        os.makedirs(new_path)
        # 让create_ftp函数在子线程中运行
        thread = threading.Thread(target=compressDealFile(path=path, basePath=path, newDirName=newDirName), args=())
        # 下面是设置守护线程：如果在程序中将子线程设置为守护线程，则该子线程会在主线程结束时自动退出
        # thread.daemon(True)
        thread.start()  # 启动线程
        log_string.set('操作结束')
    else:
        print('路径不存在')
        log_string.set('路径不存在:'+path)


def compressDealFile(path: str, basePath: str, newDirName: str):
    filenames = os.listdir(path)
    for name in filenames:
        # 全路径
        file_all_path = os.path.join(path, name)
        after_path = file_all_path.replace(basePath+'/', '')
        if after_path.split('/')[-1].startswith('.'):
            continue
        
        if os.path.isfile(file_all_path):
            subs = name.split('.')
            file_sub = subs[-1].lower()
            # 文件名称
            file_name = name.replace('.'+file_sub, '')
            file_path_name = after_path.replace(name, file_name)
            file_path_name = file_path_name.replace(' ','\ ')
            if file_sub == 'DS_Store':
                continue
            print('当前转换文件：' + file_all_path)
            log_string.set('当前转换文件:'+file_all_path)
            file_all_path = file_all_path.replace(' ','\ ')
            if ['mov', 'mp4'].__contains__(file_sub):
                cap = cv2.VideoCapture(file_all_path)  # 读取文件
                # 获取视频宽度
                frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                # 获取视频高度
                frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                if frame_width/frame_height == 4/3:
                    ffmpeg1 = FFmpeg(inputs={file_all_path:'-y'},outputs={'%s/%s/%s.mp4'%(basePath, newDirName, file_path_name):'-r 24 -s %s -max_muxing_queue_size 10240'%(select_video_ratio4_3.get())})
                    print('>>1>>>>>>>>>>>>>'+ffmpeg1.cmd)
                    ffmpeg1.run()
                    # os.system(
                    #     'ffmpeg -y -i %s -r 24 -s %s -max_muxing_queue_size 10240 %s/%s/%s.mp4' % (file_all_path, select_video_ratio4_3.get(), basePath, newDirName, file_path_name))
                else:
                    try :
                        # 24 fps 1920*1080  1280*720 3840x2160
                        ffmpeg2 = FFmpeg(inputs={file_all_path:'-y'},outputs={'%s/%s/%s.mp4'%(basePath, newDirName, file_path_name):'-r 24 -s %s -max_muxing_queue_size 10240'%(select_video_ratio16_9.get())})
                        print('>>2>>>>>>>>>>>>>'+ffmpeg2.cmd)
                        mes = ffmpeg2.run()
                        
                        # os.system(
                        #     'ffmpeg -y -i %s -r 24 -s %s -max_muxing_queue_size 10240 %s/%s/%s.mp4' % (file_all_path, select_video_ratio16_9.get(), basePath, newDirName, file_path_name))
                    except Exception as e:
                        log_string.set(str(e))
                    
                   
                # #图片水印
                # os.system("ffmpeg -i /Users/caoshixin/Desktop/未命名文件夹/video_1.mp4 -i /Users/caoshixin/Desktop/未命名文件夹/logo.png -filter_complex 'overlay=x=10:y=main_h-overlay_h-10' /Users/caoshixin/Desktop/未命名文件夹/output.mp4")
                # # 给视频加水印文字(需要brew info ffmpeg 查看支持freetype)
                # os.system("ffmpeg -i /Users/caoshixin/Desktop/未命名文件夹/video_1.mp4 -vf 'drawtext=fontfile=/Users/caoshixin/Desktop/未命名文件夹/SourceHanSansCN-Regular.ttf: text=‘技术是第一生产力’:x=10:y=10:fontsize=24:fontcolor=white:shadowy=2' /Users/caoshixin/Desktop/未命名文件夹/output.mp4")
            elif ['wav', 'mp3', 'aac', 'wma', 'cda', 'flac', 'm4a', 'mid', 'mka', 'mp2', 'mpa', 'mpc', 'ape', 'ofr', 'ogg', 'ra', 'wv', 'tta', 'ac3', 'dts'].__contains__(file_sub):
                ffmpeg3 = FFmpeg(inputs={file_all_path:None},outputs={'%s/%s/%s.mp3'%(basePath, newDirName, file_path_name):'-vn -ar 44100 -ac 2 -b:a 64k'})
                print('>>3>>>>>>>>>>>>>'+ffmpeg3.cmd)
                ffmpeg3.run_async()
                # os.system('ffmpeg -i %s -vn -ar 44100 -ac 2 -b:a 64k %s/%s/%s.mp3' %
                #           (file_all_path, basePath, newDirName, file_path_name))
            else:
                # 其余文件拷贝
                shutil.copyfile(file_all_path, basePath +
                                '/'+newDirName+'/'+after_path)
        elif os.path.isdir(file_all_path):
            if name != newDirName:
                # 如果是目录，则递归
                new_dir = os.path.join(basePath, newDirName+'/'+after_path)
                if not os.path.exists(new_dir):
                    os.makedirs(new_dir)
                compressDealFile(
                    file_all_path, basePath=basePath, newDirName=newDirName)
        else:
            print("其他情况")
            log_string.set('其他情况:'+file_all_path)
            pass

root = Tk()
root.title("曹世鑫出品:音视频转换压缩")
root.geometry("700x405+200+200")
root["background"] = "#C2E5E3"

# 初始化Entry控件的textvariable属性值
select_path = StringVar()
select_video_ratio16_9 = StringVar(value='1920*1080')
select_video_ratio4_3 = StringVar(value='1440*1080')
log_string = StringVar(value='')
# 布局控件
Label(root, text="文件路径：", background="#C2E5E3").grid(
    column=0, row=0, rowspan=3)
Entry(root, textvariable=select_path).grid(column=1, row=0, rowspan=3)
# Button(root, text="选择单个文件", command=select_file).grid(row=0, column=2)
# Button(root, text="选择多个文件", command=select_files).grid(row=1, column=2)
Button(root, text="选择文件夹", command=select_folder,
       height=5).grid(row=2, column=2)

Label(root, text='16:9视频大小', height=1,
      background="#C2E5E3").grid(row=3, column=0)
#  "1280*720","1920*1080", "3840x2160"
OptionMenu(root, select_video_ratio16_9, "1280*720",
           "1920*1080").grid(row=3, column=1)
Label(root, text='4:3视频大小', height=1,
      background="#C2E5E3").grid(row=3, column=2)
# "1440*1080","1920*1440", "2560x1920"
OptionMenu(root, select_video_ratio4_3, "1440*1080").grid(row=3, column=3)
Label(root, height=1,  background="#C2E5E3").grid(row=4, column=1)
Button(root, text='执行压缩转换处理', command=compress).grid(row=5, column=1)
Label(root, height=1,  background="#C2E5E3").grid(row=6, column=1)
Label(root, text="执行log:", background="#C2E5E3").grid(
    column=0, row=7)
Label(root, textvariable=log_string, background="#C2E5E3",width=40).grid(column=1, row=7)
Label(root, height=8, background="#C2E5E3").grid(row=8, column=1)

Button(root, text="退出", command=root.quit).grid(row=9, column=1)

root.mainloop()
