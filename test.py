import platform
import os
userPlatform=platform.system()						# 获取操作系统

fileDir=r'D:\Intersection_TF\夜晚.jpg'

if userPlatform == 'Darwin':								# Mac
    subprocess.call(['open', fileDir])
elif userPlatform == 'Linux':								# Linux
    subprocess.call(['xdg-open', fileDir])
else:																# Windows
    os.startfile(fileDir)