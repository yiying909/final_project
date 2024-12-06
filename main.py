from csv_func import write_csv, read_csv
from class_def import create_cloth, filter
from clothDecison import get_outfit
from weather import tm_get_weather
import random
from display import tm_display_images


# 获取天气信息
_, _, temp_f, _ = tm_get_weather()

# 询问用户是否要上传衣物
upload_choice = input("Do you want to upload clothing data? (yes/no): ")
if upload_choice == 'yes':
    write_csv()  # 只有在用户选择上传时才调用该函数

# 读取服装数据
clothdata = read_csv()
if not clothdata:
    print("No clothing data found in the CSV file.")
    exit()
clothes = create_cloth(clothdata)  # 创建服装实例
outfit = get_outfit(temp_f)  # 获取推荐的服装

image_paths = []
for item in outfit:
    filtered = filter(clothes, item)  # 使用 filter 函数
    if filtered:
        # 随机选择一个文件名
        random_item = random.choice(filtered)
        image_paths.append(random_item.filename)  # 添加文件名到路径列表

# 显示选择的图片
if image_paths:
    tm_display_images(image_paths)
else:
    print("No matching clothing images found.")