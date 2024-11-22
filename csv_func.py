import csv, os


    
def write_csv(fname = "clothes.csv"):
    # write or append
    with open(fname, 'a', newline="") as file:
        csv_writer = csv.writer(file)
        data = {
            "temp_min" : input("min_temp"),
            "temp_max" : input("max_temp"),
            "picture_path" : input("picture_path")}
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
        print(datalist) 

# ask for clothes
# write_csv()
# write_csv()
read_csv()