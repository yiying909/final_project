# import libraries we need
import requests
from bs4 import BeautifulSoup

def get_7dayweather(city):
    lst = []
    def get_weather(num):
        if num > 7:
            return lst
        else:
            header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}
            url = f"https://www.google.com/search?q=weather+{city}+in+{num}+day"  # Fixed URL format
            html_content = requests.get(url, headers = header).content

            # parse html into readable content
            content = BeautifulSoup(html_content, 'html.parser')
            # print(content.prettify())  # This will print out the formatted HTML to verify structure

            # find actual info needed from content: temp in °F and °C
            
            temp_f = int(content.find('span', attrs={"class" : "wob_t"}, id='wob_ttm').text)
            temp_c = int(content.find('span', attrs={'class': 'wob_t q8U8x'}, id="wob_tm").text)

            data = {
                "temp_f" : temp_f,
                "temp_c" : temp_c
            }
            lst.append(data)
            return get_weather(num+1)

    return get_weather(0)

# print(get_7dayweather("amherst"))



# ask for location and get search result; determine header to access actual attritube on webpage


def get_weather(city):
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}
    url = "https://www.google.com/search?q=" + "weather" + city
    html_content = requests.get(url, headers = header).content

    # parse html into readable content
    content = BeautifulSoup(html_content, 'html.parser')
    # print(content.prettify())  # This will print out the formatted HTML to verify structure

    # find actual info needed from content: temp in °F and °C
    temp_c = int(content.find('span', attrs={"class" : "wob_t"}, id='wob_ttm').text)
    temp_f = int(content.find('span', attrs={'class': 'wob_t q8U8x'}, id="wob_tm").text)
    real_time = content.find('div', attrs={'class': 'wob_dts'}).text
    description = content.find('div', attrs={'class': 'wob_dcp'}).text

    print(f'''Right now is {real_time},
    with temperature is {temp_f}°F/{temp_c}°C, and {description}
    ''')

    return real_time, temp_c, temp_f, description


def tm_get_weather():
    def get_city():
        location = input("where are you at? ")
        return location
    get_weather(get_city())
    

# tm_get_weather()