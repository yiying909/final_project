#main program

from csv_func import write_csv, read_csv
from class_def import create_cloth, filter
from clothDecison import get_outfit
from weather import get_weather

# need to rearrange, upload once then only last out generate feature
write_csv()
clothdata = read_csv()
print(read_csv())
clothes = create_cloth(clothdata)

# top_wear = ['T-shirt', 'Long-sleeve shirt', 'Sweater', 'Jacket', 'Heavy jacket', 'Heavy winter coat']
# bottom_wear = ['shorts', 'pants']
# footwear = ['sandals', 'sneakers', 'boots']
# accessories = ['gloves', 'scarf', 'hat']

Topwear = {
    "T-shirt" : filter(clothes, "T-shirt"),
    "Long-sleeve shirt" : filter(clothes, "Long-sleeve shirt"),
    "Sweater" : filter(clothes, "Sweater")
#so on
}

# ask for temp perference, c or f?
temp_c, temp_f = get_weather()
#get outfit and display



