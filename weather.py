# import libraries we need
import requests
from bs4 import BeautifulSoup

def get_7dayweather(city):
    lst = []
    def get_weather(num):
        if num > 7:
            return 
        else:
            header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}
            url = "https://www.google.com/search?q=" + "weather" + city
            html_content = requests.get(url, headers = header).content

            # parse html into readable content
            content = BeautifulSoup(html_content, 'html.parser')

            # find actual info needed from content: temp in °F and °C
            temp_f = int(content.find('span', attrs={'class': 'wob_t q8U8x'}).text)
            temp_c = int(content.find('span', id='wob_ttm').text)

            data = {
                "temp_f" : temp_f,
                "temp_c" : temp_c
            }
            lst.append(data)
            get_weather(num+1)





# ask for location and get search result; determine header to access actual attritube on webpage
def get_city():
    location = input("where are you at? ")
    return location

def get_weather(city):
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}
    url = "https://www.google.com/search?q=" + "weather" + city
    html_content = requests.get(url, headers = header).content

    # parse html into readable content
    content = BeautifulSoup(html_content, 'html.parser')

    # find actual info needed from content: temp in °F and °C
    temp_f = int(content.find('span', attrs={'class': 'wob_t q8U8x'}).text)
    temp_c = int(content.find('span', id='wob_ttm').text)
    real_time = content.find('div', attrs={'class': 'wob_dts'}).text
    description = content.find('div', attrs={'class': 'wob_dcp'}).text

    print(f'''Right now is {real_time},
    with temperature is {temp_f}°F/{temp_c}°C, and {description}
    ''')

    return real_time, temp_c, temp_f, description

def tm_get_weather():
    get_weather(get_city())
    
# get_weather()

# from clothDecison import get_outfit
# print(f'we recommend wearing {get_outfit(temp_f)}')