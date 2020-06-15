import requests
import json


url = "https://restapi.amap.com/v3/weather/weatherInfo?"
params = {
    'key': "0284e0544b56e0a0acca5848ef25efcd",
    'city': 110101
}

content = requests.get(url=url, params=params).content.decode()

for city_info in json.loads(content)['lives']:
    print(city_info['province'])
    print(city_info['city'])

