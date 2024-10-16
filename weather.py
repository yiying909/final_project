# import libraries we need
import requests
from bs4 import BeautifulSoup

# ask for location and get search result; determine header to access actual attritube on webpage
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}
location = input("where are you at? ")
url = "https://www.google.com/search?q=" + "weather" + location
html_content = requests.get(url, headers = header).content

# parse html into readable content
content = BeautifulSoup(html_content, 'html.parser')

# find actual info needed from content: temp in °F and °C
temp_f = content.find('span', attrs={'class': 'wob_t q8U8x'}).text
temp_c = content.find('span', id='wob_ttm').text
real_time = content.find('div', attrs={'class': 'wob_dts'}).text
description = content.find('div', attrs={'class': 'wob_dcp'}).text

print(f'''Right now is {real_time},
with temperature is {temp_f}°F/{temp_c}°C, and {description}
''')