from time import sleep
import os, shutil
usb_path = "I:\\"
des_path = r'F:\copy_usb'


# 复制I盘下的所有文件(des_path必须不存在)
while True:
    try:
        content = os.listdir(usb_path)
        print(content)
        shutil.copytree(usb_path, des_path, False)
        break
    except Exception:
        sleep(3)
