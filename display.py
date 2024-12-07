from PIL import Image, ImageTk

import os

current_dir = os.getcwd()
# print("Current Directory:", current_dir)

# 定义图片存储的默认路径
# default_dir = r'D:\CICS110\final_project\picture'

default_size = (200, 200)  # 设置默认大小为 200x200 像素

def resize_image(img):
    # 调整图像大小
    return img.resize(default_size, Image.LANCZOS)  # 使用 LANCZOS 进行高质量缩放

def display_images(image_filenames):
    image_paths = [os.path.join(current_dir, "pictures", filename) for filename in image_filenames]

    images = []
    for img_path in image_paths:
        if os.path.exists(img_path):
            img = Image.open(img_path)
            resized_img = resize_image(img)
            tk_image = ImageTk.PhotoImage(resized_img)  # Convert to Tkinter-compatible image
            images.append(tk_image)
    return images
