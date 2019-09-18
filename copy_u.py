from time import sleep
import os, shutil

usb_path = "I:\\"
# 复制I盘下的所有文件(des_path必须不存在)
des_path = r'F:\copy_usb'

# V1.0 复制所有文件
while True:
    if os.path.exists(usb_path):
        # 复制给定路径下所有文件夹及子文件夹
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
                    shutil.copy2(file, des_path)
    sleep(10)


# 判断文件大小
def getDocSize(path):
    try:
        size = os.path.getsize(path)
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return "%3.1f %s" % (size, x)
            size /= 1024.0
    except Exception as err:
        print(err)
