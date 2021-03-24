import numpy as np
from PIL import Image
from PIL import ImageDraw


def draw_test():
    # 生成深蓝色绘图画布
    array = np.ndarray((480, 640, 3), np.uint8)

    array[:, :, 0] = 0
    array[:, :, 1] = 0
    array[:, :, 2] = 100

    image = Image.fromarray(array)

    # 创建绘制对象
    draw = ImageDraw.Draw(image)

    # 绘制直线
    draw.line((20, 20, 150, 150), 'cyan')

    # 绘制矩形
    draw.rectangle((100, 200, 300, 400), 'black', 'red')

    image.show()


if __name__ == '__main__':
    draw_test()
