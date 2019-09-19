from time import sleep
import os, shutil
import re

usb_path = "I:\\"
des_path = r'F:\copy_usb'

# V1.0 复制U盘所有文件
while True:
    if os.path.exists(usb_path):
        # 复制给定路径下所有文件夹及子文件夹, des_path必须不存在
        shutil.copytree(usb_path, des_path, False)
        break
    sleep(3)


# V2.0 根据文件大小复制文件
while True:
    if os.path.exists(usb_path):
        for root, dir, files in os.walk(usb_path):
            for name in files:
                file = os.path.join(root, name)
                if os.path.getsize(file) < 3*1024*1024:
                    # copy2()下des_path必须存在
                    shutil.copy2(file, des_path)
        break
    sleep(10)


def getDocSize(path):
    try:
        size = os.path.getsize(path)
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return "%3.1f %s" % (size, x)
            size /= 1024.0
    except Exception as err:
        print(err)


# V3.0 根据文件类型复制文件
while True:
    if os.path.exists(usb_path):
        for root, dir, files in os.walk(usb_path):
            for name in files:
                file = os.path.join(root, name)
                # 可以加入大小判断 and os.path.getsize(file) < 3*1024*1024:
                if re.findall('(.*zip$)|(.*rar$)|(.*docx$)|(.*ppt$)|(.*xls$)|(.*txt$)|(.*jpg$)', file):
                    shutil.copy2(file, des_path)
        break
    sleep(10)
