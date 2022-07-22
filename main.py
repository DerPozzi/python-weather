import requests
from geopy.geocoders import Nominatim

apiKey = "95b5a2960c4a91337c38d65b39d55cfb"
url = f"https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid={apiKey}"

res = requests.get(url)

print(res)