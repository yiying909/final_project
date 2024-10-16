# Importing necessary libraries
import requests
from bs4 import BeautifulSoup

# Enter city name
city = input("Enter where you at? ")

# Creating URL and making requests instance
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}
url = "https://www.google.com/search?q=" + "weather" + city
html = requests.get(url, headers = header).content

# Getting raw data using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Extracting the temperature
# temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
temp = soup.find('span', attrs={'class': 'wob_t q8U8x'}).text

# Extracting the time and sky description
# str_ = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
# data = str_.split('\n')
# time = data[0]
# sky = data[1]


# Printing the extracted weather data
# print("Temperature is:", temp)
# print("Time:", time)
# print("Sky Description:", sky)


