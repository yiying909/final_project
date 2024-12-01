import csv, os
topwear = ['T-shirt', 'Long-sleeve shirt', 'Sweater', 'Jacket', 'Heavy jacket', 'Heavy winter coat']
bottomwear = ['shorts', 'pants']
footwear = ['sandals', 'sneakers', 'boots']
accessories = ['gloves', 'scarf', 'hat']

def get_type():
    types = input(f'''
which type of clothes it is?
options: a)topwear b)bottomwear c)footwear d)accessories
    enter here: ''')
    if types not in {"topwear","bottomwear", "footwear","accessories"}:
        print("Please enter valid type name.")
        return get_type()          
    return types

def get_subtype(types):
    if types == "topwear":
        result = input(f'''
enter which type of it is?
options: {topwear}
enter here: ''')
    elif types == "bottomwear":
        result = input(f'''
enter which type of it is?
options: {bottomwear}
enter here: ''') 
    elif types == "footwear":
        result = input(f'''
enter which type of it is?
options: {footwear}
enter here: ''')
    elif types == "accessories":
        result = input(f'''
enter which type of it is?
options: {accessories}
enter here: ''')  
    if result not in topwear+bottomwear+footwear+accessories:
        print("please enter a valid subtype name")
        return get_subtype(types)
    return result

def write_csv(fname = "clothes.csv"):
    # write or append?
    with open(fname, 'a', newline="") as file:
        csv_writer = csv.writer(file)
        # csv_writer.writewrow(f'filename,type')
        num = input("how many pieces of cloth are you gonna upload?")
        try:
            num = int(num)  # 检查输入是否为整数
        except ValueError:
            print("Please enter a valid number.")
            return
        
        for i in range(num):
            types = get_type()
            result = get_subtype(types)
            filename = input("enter the image file name: ")
            if not filename:
                print("File name cannot be empty.")
                continue  # 跳过此次循环
            
            data = {
                "filename": filename,
                "type": result
            }        
            # display clothes data
            csv_writer.writerow(value for value in data.values())

    
def read_csv(fname="clothes.csv"):
    datalist = []
    with open(fname, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if not row:
                continue  # 跳过空行
            datalist.append(row)
    return datalist



# ask for clothes
write_csv()
# write_csv()
clothes_data = read_csv()
print(clothes_data)