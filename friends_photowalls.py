import itchat, os, math
from PIL import Image

# 获取微信好友头像生成照片墙


# 判断目录是否存在
def get_dir():
    if not os.path.exists('image'):
        os.mkdir('image')
    return 'image'


# 登录微信获取好友头像
def get_img(path, cnt=0):
    itchat.auto_login(hotReload=True)
    fridends = itchat.get_friends(update=True)
    for i in fridends:
        img = itchat.get_head_img(userName=i['UserName'])
        with open(os.path.join(path, str(cnt) + '.jpg'), 'wb') as fp:
            fp.write(img)
        cnt += 1
    return cnt


# 生成照片墙
def get_photo_wall(path, cnt):
    # 计算每行图片的个数
    row = int(math.sqrt(cnt)) + 1
    # 定义每个图片的大小50*50
    origin = 50

    new_img = Image.new('RGB', (row*50, row*50), 'white')
    # 定义图片初始位置
    
    x = y = 0
    img_list = os.listdir('image')
    # 粘贴图片
    for img in img_list:
        im = Image.open(os.path.join(path, img))
        im = im.resize((origin, origin), Image.ANTIALIAS)
        new_img.paste(im, (x*origin, y*origin))
        x += 1
        if x == row:
            x = 0
            y += 1
            
    new_img.save('photo_walls.jpg')


path = get_dir()
result = get_img(path)
get_photo_wall(path, result)
