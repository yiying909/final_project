import csv, os
topwear = ['T-shirt', 'Long-sleeve shirt', 'Sweater', 'Jacket', 'Heavy jacket', 'Heavy winter coat']
bottomwear = ['shorts', 'pants']
footwear = ['sandals', 'sneakers', 'boots']
accessories = ['gloves', 'scarf', 'hat']

def write_csv(fname = "clothes.csv"):
    # write or append?
    with open(fname, 'a', newline="") as file:
        csv_writer = csv.writer(file)
        # csv_writer.writewrow(f'filename,type')
        num = input("how many pieces of cloth are you gonna upload?")
        for i in range(int(num)):
            types = input(f'''
which type of clothes it is?
options: a)topwear
    enter here: ''')
            if types == "topwear":
                result = input(f'''
enter which type of it is?
options: {topwear}
    enter here: ''')
                # how to simplify this part above
            data = {
                "filename" : input("enter the image file name: "),
                "type" : result
                }
            # display clothes data
            csv_writer.writerow(value for value in data.values())

    
def read_csv(fname = "clothes.csv"):
    datalist = []
    with open(fname, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if not row:
                return None
            datalist.append(row)
    if datalist:
        return datalist

# ask for clothes
# write_csv()
# write_csv()
read_csv()