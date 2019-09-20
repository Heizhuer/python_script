from PIL import Image

# 生成九宫格图片

# 图片路径
jpg = ''
image = Image.open(jpg)


def fill_image(image):
    width, height = image.size
    new_length = max(width, height)

    new_image = Image.new(image.mode, (new_length, new_length), 'white')

    # 如果宽度大于高度, 则背景颜色在上下, 否则在左右
    if width > height:
        new_image.paste(image, (0, (width - height / 2)))
    else:
        new_image.paste(image, (height - width / 2, 0))

    return new_image


def cut_img(image):
    # 朋友圈每行为三张图片
    cut_width = image.size[0] / 3
    # 存放每个小图片的位置
    box_list = []

    for i in range(3):
        for j in range(3):
            left = i*cut_width
            upper = j*cut_width
            right = (i + 1)*cut_width
            lower = (j + i)*cut_width

            box_list.append((left, upper, right, lower))
    # 通过剪裁获得每个小图片
    img_list = [image.crop(i) for i in box_list]

    return img_list


def save_img(img_list):
    index = 1
    # 保存每个小图片
    for img in img_list:
        img.save(str(index) + '.jpg')
        index += 1
