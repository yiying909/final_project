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

def tm_display_images(image_filenames):
    image_paths = [os.path.join(current_dir, "tmpictures", f"{filename}.png") for filename in image_filenames]

    images = []
    for img_path in image_paths:
        if os.path.exists(img_path):
            img = Image.open(img_path)
            resized_img = resize_image(img)
            images.append(resized_img)
            ## for app, above is good enough
        else:
            print(f"Image {img_path} not found.")

    if not images:
        print("No valid images found.")
        return

    # 计算总高度和最大宽度
    total_height = sum(img.height for img in images)
    max_width = max(img.width for img in images)

    # 创建新图像以合成所有图片
    new_image = Image.new('RGBA', (max_width, total_height))

    current_height = 0
    for img in images:
        new_image.paste(img, (0, current_height))
        current_height += img.height

    new_image.show()  # 显示合成的图像


#a= ['boots1', 'boots2', 'sweater3'] 
#display_images(a)
