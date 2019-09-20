from removebg import RemoveBg
from PIL import Image

rmbg = RemoveBg('sy4J7ujaEBLNWWLHYyubbuZx', 'error_log')
# 在原照片路径下生成png图片
rmbg.remove_background_from_img_file(r'white.jpg')


# 更改证件照底色
im = Image.open('white.jpg_no_bg.png')
x, y = im.size

p = Image.new(im.mode, im.size, 'red')
p.paste(im, (0, 0), im)
p.save('red.png')

# 网址: https://www.remove.bg
