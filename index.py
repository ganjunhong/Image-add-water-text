from PIL import Image, ImageDraw, ImageFont
from PIL import Image, ImageDraw, ImageFont, ImageOps
import math

#横向添加水印
def add_text_watermark(input_image_path, output_image_path, watermark_text):
    # 打开图像
    original_image = Image.open(input_image_path)

    # 创建一个可以在图像上绘制的对象
    draw = ImageDraw.Draw(original_image)

    # 设置水印文本的颜色
    text_color = (255, 255, 255)  # 白色

    # 获取图像的尺寸
    image_width, image_height = original_image.size

    # 计算水印在x轴上的数量和间隔
    num_watermarks_x = 3
    x_interval = image_width // (num_watermarks_x + 1)

    # 计算水印在y轴上的数量和间隔
    num_watermarks_y = 5
    y_interval = image_height // (num_watermarks_y + 1)

    # 计算合适的字体大小
    font_size = min(image_width // 20, image_height // 20)

    # 选择字体和大小
    # 选择字体和大小（使用SimHei.ttf作为中文字体）
    font_path = "./otf/SourceHanSansCN-Normal.ttf"
    font = ImageFont.truetype(font_path, font_size)

    # 在图像上绘制水印
    for i in range(num_watermarks_x):
        for j in range(num_watermarks_y):
            x = (i + 1) * x_interval - font_size // 2
            y = (j + 1) * y_interval - font_size // 2

            draw.text((x, y), watermark_text, font=font, fill=text_color)

    # 保存带有水印的图像
    original_image.save(output_image_path)
#旋转添加水印方法
def add_rotated_text_watermarks(input_image_path, output_image_path, watermark_text):
    # 打开图像
    original_image = Image.open(input_image_path)

    # 创建一个可以在图像上绘制的对象
    draw = ImageDraw.Draw(original_image)
    # 设置水印文本的颜色
    opacity=128
    text_color = (255, 255, 255,opacity)  # 白色
    # 获取图像的尺寸
    image_width, image_height = original_image.size
    # 计算水印在x轴上的数量和间隔
    num_watermarks_x = 3
    x_interval = image_width // (num_watermarks_x + 1)
    # 计算水印在y轴上的数量和间隔
    num_watermarks_y = 5
    y_interval = image_height // (num_watermarks_y + 1)
    # 计算合适的字体大小
    font_size = min(image_width // 20, image_height // 20)
    # 选择字体和大小（使用SimHei.ttf作为中文字体）
    font_path = "./otf/SourceHanSansCN-Normal.ttf"
    font = ImageFont.truetype(font_path, font_size)

    # 在图像上绘制斜向上45度旋转的水印
    for i in range(num_watermarks_x):
        for j in range(num_watermarks_y):
            x = (i + 1) * x_interval - font_size // 2
            y = (j + 1) * y_interval - font_size // 2

            # 创建旋转后的水印
            rotated_text = Image.new('RGBA', (font_size * 4, font_size * 4), (0, 0, 0, 0))
            rotated_text_draw = ImageDraw.Draw(rotated_text)
            rotated_text_draw.text((0, 0), watermark_text, font=font, fill=text_color)
            # 旋转角度为45度
            rotated_text = rotated_text.rotate(45, resample=Image.BICUBIC, expand=True)
            # 将旋转后的水印粘贴到原始图像上
            original_image.paste(rotated_text, (x, y), rotated_text)
    # 保存带有水印的图像
    original_image.save(output_image_path)

# 示例用法
input_image_path = './static/5.jpg'  # 替换为输入图像的路径
output_image_path = './static/6.jpg'  # 替换为输出图像的路径
watermark_text = '试用水印'  # 替换为你想要的水印文本

add_rotated_text_watermarks(input_image_path, output_image_path, watermark_text)
